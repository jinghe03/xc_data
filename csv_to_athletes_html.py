import csv
import os

def process_athlete_data(file_path):

   # Extracting athlete stats by year
   records = []

   # Extracting athlete races
   races = []

   athlete_name = ""
   athlete_id = ""
   comments = ""

   with open(file_path, newline='', encoding='utf-8') as file:
      reader = csv.reader(file)
      data = list(reader)

      athlete_name = data[0][0]
      athlete_id = data[1][0]
      print(f"The athlete id for {athlete_name} is {athlete_id}")

      for row in data[5:-1]:
         if row[2]:
            records.append({"year": row[2], "sr": row[3]})
         else:
            races.append({
               "finish": row[1],
               "time": row[3],
               "meet": row[5],
               "url": row[6],
               "comments": row[7]
            })

   return {
      "name": athlete_name,
      "athlete_id": athlete_id,
      "season_records": records,
      "race_results": races,
      "comments": comments
   }

def gen_athlete_page(data, outfile):
   # Define default image path
   # default_image = "../images/default_image.jpg"
   # athlete_image_path = f"images/profiles/{data['athlete_id']}.jpg"

   # # Check if the athlete's image exists
   # if not os.path.exists(athlete_image_path):
   #    athlete_image_path = default_image  # Use the default image if not found
   # else:
   #    athlete_image_path = f"../images/profiles/{data['athlete_id']}.jpg"

   # template
   # Start building the HTML structure
   html_content = f'''<!DOCTYPE html>
   <html lang="en">
   <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">


      <link rel = "stylesheet" href = "../css/reset.css">
      <link rel = "stylesheet" href = "../css/style.css">
      <link rel="stylesheet" href="../dist/css/lightbox.css"/>


      <title>{data["name"]}</title>
   </head>
   <body>

   <a href = "#main" class="skip-link">Skip to Main Content</a>

   <!-- Fixed Header with Banner -->
   <header class="banner" aria-label="Main banner">
      <!-- Expandable Menu Button -->
      <button id="menu-toggle" class="menu-button" aria-label="Toggle menu">☰ Menu</button>

      <h1>Profile</h1>
   </header>

   <nav id="side-menu" class="side-menu hidden">
      <ul>
         <li><a href="../index.html">Home Page</a></li>
         <li><a href="../mens.html">Men's Team</a></li>
         <li><a href="../womens.html">Women's Team</a></li>
      </ul>
   </nav>




   <main id = "main">
   <div class="header-container">
         <!--Athlete would input headshot-->
         <h1>{data["name"]}</h1>

         <!-- Lightbox link wrapping the headshot -->
         <a href="../images/profiles/{data["athlete_id"]}.jpg" data-lightbox="profile" data-title="{data['name']}">
         <img class="fade-in" src="../images/profiles/{data["athlete_id"]}.jpg" alt="Athlete headshot" width="200">
         </a>

      </div>

      <section id= "athlete-sr-table">
         <h2>Athlete's Seasonal Records (SR) per Year</h2>
            <table>
                  <thead>
                     <tr>
                        <th> Year </th>
                        <th> Season Record (SR)</th>
                     </tr>
                  </thead>
                  <tbody>
                  '''

   for sr in data["season_records"]:
      sr_row = f'''
                     <tr>
                        <td>{sr["year"]}</td>
                        <td>{sr["sr"]}</td>
                     </tr>
               '''
      html_content += sr_row

   html_content += '''
               </tbody>
                  </table>
                     </section>

                     <details>
                        <summary>Race Results</summary>

                        <section id="athlete-result-table">


                           <table id="athlete-table">
                              <thead>
                                 <tr>
                                    <th>Race</th>
                                    <th>Athlete Time</th>
                                    <th>Athlete Place</th>
                                    <th>Race Comments</th>
                                 </tr>
                              </thead>

                              <tbody>
                  '''

   # add each race as a row into the race table 
   for race in data["race_results"]:
      race_row = f'''
                                 <tr class="result-row">
                                    <td data-label="Race">
                                       <a href="{race["url"]}">{race["meet"]}</a>
                                    </td>
                                    <td data-label="Time">{race["time"]}</td>
                                    <td data-label="Place">{race["finish"]}</td>
                                    <td data-label="Comments">{race["comments"]}</td>
                                 </tr>
      '''
      html_content += race_row

   html_content += '''
                              </tbody>
                           </table>
                        </details>
                     </section>
                     <section id = "gallery">
                     <h2>Gallery</h2>
                     </section>
                     </main>
                     <footer>
                     <p>
                     Skyline High School<br>
                     <address>
                     2552 North Maple Road<br>
                     Ann Arbor, MI 48103<br><br>

                     <a href = "https://sites.google.com/aaps.k12.mi.us/skylinecrosscountry2021/home" aria-label="Visit the Skyline Cross Country official page">XC Skyline Page</a><br>
                     Follow us on Instagram <a href="https://www.instagram.com/a2skylinexc/"> @a2skylinexc</a>

                     </p>
                     </footer>

                     <!-- Link to the JavaScript file -->
                     <script src="../js/script.js"></script>
                     <script src="../dist/js/lightbox-plus-jquery.js"></script>
                     <script>
                     document.addEventListener("DOMContentLoaded", function() {
                        document.querySelectorAll('img').forEach(img => {
                           img.onerror = function() {
                                 this.onerror = null; // Prevents infinite loop if default image also fails
                                 this.src = '../images/default_image.jpg'; // Path to default image
                                 this.alt = ""; // Alt text for the default image
                                 const link = this.closest('a');
                                 if (link) {
                                    link.href = '../images/default_image.jpg';
                                 }
                           };
                        });
                     });
                  </script>
               </body>
         </html>
   '''

   with open(outfile, 'w') as output:
      output.write(html_content)


def main():

   import os
   import glob

   # Define the folder path
   folder_path = 'mens_team/'
   # Get all csv files in the folder
   csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

   # Extract just the file names (without the full path)
   csv_file_names = [os.path.basename(file) for file in csv_files]

   # Output the list of CSV file names
   print(csv_file_names)
   for file in csv_file_names:

      # read data from file
      athlete_data = process_athlete_data("mens_team/"+file)
      # using data to generate templated athlete page
      gen_athlete_page(athlete_data, "mens_team/"+file.replace(".csv",".html"))

      # read data from file
      # athlete_data2 = process_athlete_data(filename2)
      # using data to generate templated athlete page
      # gen_athlete_page(athlete_data2, "enshu_kuan.html")


   # Define the folder path
   folder_path = 'womens_team/'
   # Get all csv files in the folder
   csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

   # Extract just the file names (without the full path)
   csv_file_names = [os.path.basename(file) for file in csv_files]

   # Output the list of CSV file names
   print(csv_file_names)
   for file in csv_file_names:

      # read data from file
      athlete_data = process_athlete_data("womens_team/"+file)
      # using data to generate templated athlete page
      gen_athlete_page(athlete_data, "womens_team/"+file.replace(".csv",".html"))

      # read data from file
      # athlete_data2 = process_athlete_data(filename2)
      # using data to generate templated athlete page
      # gen_athlete_page(athlete_data2, "enshu_kuan.html")

if __name__ == '__main__':
   main()

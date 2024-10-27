# List of men athlete file names
csv_file_names_men = [
    'Paxton Rose23349712.csv', 'Caspian Ruiz26460414.csv', 'Rowan Kim24801855.csv', 'Gustaf Finn21147171.csv', 
    'Oskar MacArthur23349698.csv', 'Connor Jett24801564.csv', 'Jackson Cichewicz26322046.csv', 'Nicholas Yuan21615273.csv', 
    'Lawrence Wang26460421.csv', 'Martin Gehrke19203161.csv', "Sage O'Lor26322021.csv", 'Dylan Hanley23349680.csv', 
    'Leo Chi26460401.csv', 'Loki Bowser21147175.csv', 'Zeke Lafferty21142917.csv', 'Alex Nemecek18820260.csv', 
    'Garrett Comer21615274.csv', 'Micah Winchell21147172.csv', 'Amir Abston25395576.csv', 'Jude Shafer23349716.csv', 
    'Henry Strait22288700.csv', 'Leland Weiser18820273.csv', 'Joowon Lee23349696.csv', 'Marlowe Hartnett21147174.csv', 
    'Evan Leach26322027.csv', 'Cole Harms26322018.csv', 'Parker Razelun18820257.csv', 'Juan Luis Llanes23564880.csv', 
    'Roman Stilwell25989957.csv', 'Phylip Elliott23636797.csv', 'Jack Robichaud18820279.csv', 'William Johnson23564879.csv', 
    'Emmett Strait26322025.csv', 'Enshu Kuan23687884.csv', 'Elliot Daley26322015.csv', 'Matthew Guikema23349678.csv', 
    'Bruno Cifaldi21147176.csv', 'Ethan Miller23349703.csv', 'Ezekiel Paloff23349707.csv', 'Santiago Valenzuela23821078.csv', 
    'Kyle Krasan21245954.csv', 'Raphael Fournier23564875.csv'
]

# Generate HTML list items for all men athletes
for index, file in enumerate(csv_file_names_men, start=1):
    # Convert file name to HTML reference (change .csv to .html)
    html_file = file.replace('.csv', '.html')
    
    # Extract the athlete's name from the file name (up to the numbers)
    athlete_name = ''.join([c for c in file.split('.')[0] if not c.isdigit()]).strip()
    
    # Generate and print the HTML list item
    print(f'<li><a href="mens_team/{html_file}">{athlete_name} (Athlete {index})</a></li>')

# List of women athlete file names
csv_file_names_women = [
    'Ayla Balazer19352189.csv', 'Lucia Llanes26328690.csv', 'Ann Kececi24802381.csv', 'Arabella Kessler23564883.csv', 'Nina Beals23564881.csv', 
    'Ruthie Scott23349715.csv', 'Katie Yuan23349724.csv', 'Elin Tenbrink23349718.csv', 'Julianna Heung23687880.csv', 'Alexandra Wren21142908.csv', 
    'Grace Hopkins21142901.csv', 'Gwen Stotts-Walshe24802677.csv', 'Emily Mei22520376.csv', 'Becca Van Lent24262808.csv', 'Lila Edison23349671.csv', 
    'Calla Sopoci26328689.csv', 'LeAnne Fayyad24802883.csv', 'Alison Kauffman23564882.csv', 'Mara Mocanu23687883.csv', 'Lily Greenberg23687875.csv', 
    'Adrienne Stewart21142907.csv', 'Livi Byers26322051.csv', 'Pia Odell26328678.csv', 'Tia Cocciolone22520342.csv', 'Irie Scrase23564884.csv', 
    'Cecilia DeGuzman21142897.csv', 'Isla Tharp23349719.csv', 'Elsa Wenzlaff22520388.csv', 'Violet Olley26328683.csv', 'Vera Naines18895017.csv'
]

# Generate HTML list items for all women athletes
for index, file in enumerate(csv_file_names_women, start=1):
    # Convert file name to HTML reference (change .csv to .html)
    html_file = file.replace('.csv', '.html')
    
    # Extract the athlete's name from the file name (up to the numbers)
    athlete_name = ''.join([c for c in file.split('.')[0] if not c.isdigit()]).strip()
    
    # Generate and print the HTML list item
    print(f'<li><a href="womens_team/{html_file}">{athlete_name} (Athlete {index})</a></li>')
    

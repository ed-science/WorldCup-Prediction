groups = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H"
]

country_codes = {
    "Egypt": "eg",
    "Russia": "ru",
    "Saudi Arabia": "sa",
    "Uruguay": "uy",
    
    "IR Iran": "ir",
    "Iran": "ir",
    "Morocco": "ma",
    "Portugal": "pt",
    "Spain": "es",
    
    "Australia": "au",
    "Denmark": "dk",
    "France": "fr",
    "Peru": "pe",
    
    "Argentina": "ar",
    "Croatia": "hr",
    "Iceland": "is",
    "Nigeria": "ng",
    
    "Brazil": "br",
    "Costa Rica": "cr",
    "Serbia": "rs",
    "Switzerland": "ch",
    
    "Germany": "de",
    "Mexico": "mx",
    "Korea Republic": "kr",
    "Sweden": "se",
    
    "Belgium": "be",
    "England": "gb",
    "Panama": "pa",
    "Tunisia": "tn",
    
    "Colombia": "co",
    "Japan": "jp",
    "Poland": "pl",
    "Senegal": "sn",
}

team_players = {
    "Egypt": ["Essam El-Hadary", "Ali Gabr", "Ahmed Elmohamady", "Omar Gaber", "Sam Morsy", "Ahmed Hegazi", "Ahmed Fathy", "Tarek Hamed", "Marwan Mohsen", "Mohamed Salah", "Kahraba", "Ayman Ashraf", "Mohamed Abdel-Shafy", "Ramadan Sobhi", "Mahmoud Hamdy", "Sherif Ekramy", "Mohamed Elneny", "Shikabala", "Abdallah Said", "Saad Samir", "Trézéguet", "Amr Warda", "Mohamed El-Shenawy"], 
    
    "Russia": ["Igor Akinfeev", "Mário Fernandes", "Ilya Kutepov", "Sergei Ignashevich", "Andrei Semyonov", "Denis Cheryshev", "Daler Kuzyayev", "Yury Gazinsky", "Alan Dzagoev", "Fyodor Smolov", "Roman Zobnin", "Andrey Lunyov", "Fyodor Kudryashov", "Vladimir Granat", "Aleksei Miranchuk", "Anton Miranchuk", "Aleksandr Golovin", "Yuri Zhirkov", "Aleksandr Samedov", "Vladimir Gabulov", "Aleksandr Yerokhin", "Artem Dzyuba", "Igor Smolnikov"], 
    
    "Saudi Arabia": ["Abdullah Al-Mayouf", "Mansoor Al-Harbi", "Osama Hawsawi", "Ali Al-Bulaihi", "Omar Hawsawi", "Mohammed Al-Breik", "Salman Al-Faraj", "Yahya Al-Shehri", "Hattan Bahebri", "Mohammad Al-Sahlawi", "Abdulmalek Al-Khaibri", "Mohamed Kanno", "Yasser Al-Shahrani", "Abdullah Otayf", "Abdullah Al-Khaibari", "Housain Al-Mogahwi", "Taisir Al-Jassim", "Salem Al-Dawsari", "Fahad Al-Muwallad", "Muhannad Assiri", "Yasser Al-Mosailem", "Mohammed Al-Owais", "Motaz Hawsawi"], 
    
    "Uruguay": ["Fernando Muslera", "José Giménez", "Diego Godín", "Guillermo Varela", "Carlos Sánchez", "Rodrigo Bentancur", "Cristian Rodríguez", "Nahitan Nández", "Luis Suárez", "Giorgian De Arrascaeta", "Cristhian Stuani", "Martín Campaña", "Gastón Silva", "Lucas Torreira", "Matías Vecino", "Maxi Pereira", "Diego Laxalt", "Maxi Gómez", "Sebastián Coates", "Jonathan Urretaviscaya", "Edinson Cavani", "Martín Cáceres", "Martín Silva"], 
    
    "IR Iran": ["Alireza Beiranvand", "Mehdi Torabi", "Ehsan Hajsafi", "Rouzbeh Cheshmi", "Milad Mohammadi", "Saeid Ezatolahi", "Masoud Shojaei", "Morteza Pouraliganji", "Omid Ebrahimi", "Karim Ansarifard", "Vahid Amiri", "Mohammad Rashid Mazaheri", "Mohammad Reza Khanzadeh", "Saman Ghoddos", "Pejman Montazeri", "Reza Ghoochannejhad", "Mehdi Taremi", "Alireza Jahanbakhsh", "Majid Hosseini", "Sardar Azmoun", "Ashkan Dejagah", "Amir Abedzadeh", "Ramin Rezaeian"], 
    
    "Morocco": ["Yassine Bounou", "Achraf Hakimi", "Hamza Mendyl", "Manuel da Costa", "Medhi Benatia", "Romain Saïss", "Hakim Ziyech", "Karim El Ahmadi", "Ayoub El Kaabi", "Younès Belhanda", "Fayçal Fajr", "Munir Mohamedi", "Khalid Boutaïb", "Mbark Boussoufa", "Youssef Aït Bennasser", "Nordin Amrabat", "Nabil Dirar", "Amine Harit", "Youssef En-Nesyri", "Aziz Bouhaddouz", "Sofyan Amrabat", "Ahmed Reda Tagnaouti", "Mehdi Carcela"], 
    
    "Portugal": ["Rui Patrício", "Bruno Alves", "Pepe", "Manuel Fernandes", "Raphaël Guerreiro", "José Fonte", "Cristiano Ronaldo", "João Moutinho", "André Silva", "João Mário", "Bernardo Silva", "Anthony Lopes", "Rúben Dias", "William Carvalho", "Ricardo Pereira", "Bruno Fernandes", "Gonçalo Guedes", "Gelson Martins", "Mário Rui", "Ricardo Quaresma", "Cédric", "Beto", "Adrien Silva"], 
    
    "Spain": ["David de Gea", "Dani Carvajal", "Gerard Piqué", "Nacho", "Sergio Busquets", "Andrés Iniesta", "Saúl", "Koke", "Rodrigo", "Thiago", "Lucas Vázquez", "Álvaro Odriozola", "Kepa Arrizabalaga", "César Azpilicueta", "Sergio Ramos", "Nacho Monreal", "Iago Aspas", "Jordi Alba", "Diego Costa", "Marco Asensio", "David Silva", "Isco", "Pepe Reina"], 
    
    "Australia": ["Mathew Ryan", "Milos Degenek", "James Meredith", "Tim Cahill", "Mark Milligan", "Matthew Jurman", "Mathew Leckie", "Massimo Luongo", "Tomi Juric", "Robbie Kruse", "Andrew Nabbout", "Brad Jones", "Aaron Mooy", "Jamie Maclaren", "Mile Jedinak", "Aziz Behich", "Daniel Arzani", "Danny Vukovic", "Josh Risdon", "Trent Sainsbury", "Dimitri Petratos", "Jackson Irvine", "Tom Rogic"], 
    
    "Denmark": ["Kasper Schmeichel", "Michael Krohn-Dehli", "Jannik Vestergaard", "Simon Kjær", "Jonas Knudsen", "Andreas Christensen", "William Kvist", "Thomas Delaney", "Nicolai Jørgensen", "Christian Eriksen", "Martin Braithwaite", "Kasper Dolberg", "Mathias Jørgensen", "Henrik Dalsgaard", "Viktor Fischer", "Jonas Lössl", "Jens Stryger Larsen", "Lukas Lerager", "Lasse Schöne", "Yussuf Poulsen", "Andreas Cornelius", "Frederik Rønnow", "Pione Sisto"], 
    
    "France": ["Hugo Lloris", "Benjamin Pavard", "Presnel Kimpembe", "Raphaël Varane", "Samuel Umtiti", "Paul Pogba", "Antoine Griezmann", "Thomas Lemar", "Olivier Giroud", "Kylian Mbappé", "Ousmane Dembélé", "Corentin Tolisso", "N'Golo Kanté", "Blaise Matuidi", "Steven Nzonzi", "Steve Mandanda", "Adil Rami", "Nabil Fekir", "Djibril Sidibé", "Florian Thauvin", "Lucas Hernández", "Benjamin Mendy", "Alphonse Areola"],
    
    "Peru": ["Pedro Gallese", "Alberto Rodríguez", "Aldo Corzo", "Anderson Santamaría", "Miguel Araujo", "Miguel Trauco", "Paolo Hurtado", "Christian Cueva", "Paolo Guerrero", "Jefferson Farfán", "Raúl Ruidíaz", "Carlos Cáceda", "Renato Tapia", "Andy Polo", "Christian Ramos", "Wilder Cartagena", "Luis Advíncula", "André Carrillo", "Yoshimar Yotún", "Edison Flores", "José Carvallo", "Nilson Loyola", "Pedro Aquino"], 
    
    "Argentina": ["Nahuel Guzmán", "Gabriel Mercado", "Nicolás Tagliafico", "Cristian Ansaldi", "Lucas Biglia", "Federico Fazio", "Éver Banega", "Marcos Acuña", "Gonzalo Higuaín", "Lionel Messi", "Ángel Di María", "Franco Armani", "Maximiliano Meza", "Javier Mascherano", "Enzo Pérez", "Marcos Rojo", "Nicolás Otamendi", "Eduardo Salvio", "Sergio Agüero", "Giovani Lo Celso", "Paulo Dybala", "Cristian Pavón", "Willy Caballero"], 
    
    "Croatia": ["Dominik Livaković", "Šime Vrsaljko", "Ivan Strinić", "Ivan Perišić", "Vedran Ćorluka", "Dejan Lovren", "Ivan Rakitić", "Mateo Kovačić", "Andrej Kramarić", "Luka Modrić", "Marcelo Brozović", "Lovre Kalinić", "Tin Jedvaj", "Filip Bradarić", "Duje Ćaleta-Car", "Nikola Kalinić", "Mario Mandžukić", "Ante Rebić", "Milan Badelj", "Marko Pjaca", "Domagoj Vida", "Josip Pivarić", "Danijel Subašić"], 
    
    "Iceland": ["Hannes Þór Halldórsson", "Birkir Már Sævarsson", "Samúel Friðjónsson", "Albert Guðmundsson", "Sverrir Ingi Ingason", "Ragnar Sigurðsson", "Jóhann Berg Guðmundsson", "Birkir Bjarnason", "Björn Bergmann Sigurðarson", "Gylfi Sigurðsson", "Alfreð Finnbogason", "Frederik Schram", "Rúnar Alex Rúnarsson", "Kári Árnason", "Hólmar Örn Eyjólfsson", "Ólafur Ingi Skúlason", "Aron Gunnarsson", "Hörður Björgvin Magnússon", "Rúrik Gíslason", "Emil Hallfreðsson", "Arnór Ingvi Traustason", "Jón Daði Böðvarsson", "Ari Freyr Skúlason"], 
    
    "Nigeria": ["Ikechukwu Ezenwa", "Brian Idowu", "Elderson Echiéjilé", "Wilfred Ndidi", "William Troost-Ekong", "Leon Balogun", "Ahmed Musa", "Oghenekaro Etebo", "Odion Ighalo", "John Obi Mikel", "Victor Moses", "Shehu Abdullahi", "Simeon Nwankwo", "Kelechi Iheanacho", "Joel Obi", "Daniel Akpeyi", "Ogenyi Onazi", "Alex Iwobi", "John Ogu", "Chidozie Awaziem", "Tyronne Ebuehi", "Kenneth Omeruo", "Francis Uzoho"], 
    
    "Brazil": ["Alisson", "Thiago Silva", "Miranda", "Pedro Geromel", "Casemiro", "Filipe Luís", "Douglas Costa", "Renato Augusto", "Gabriel Jesus", "Neymar", "Philippe Coutinho", "Marcelo", "Marquinhos", "Danilo", "Paulinho", "Cássio", "Fernandinho", "Fred", "Willian", "Roberto Firmino", "Taison", "Fagner", "Ederson"], 
    
    "Costa Rica": ["Keylor Navas", "Johnny Acosta", "Giancarlo González", "Ian Smith", "Celso Borges", "Óscar Duarte", "Christian Bolaños", "Bryan Oviedo", "Daniel Colindres", "Bryan Ruiz", "Johan Venegas", "Joel Campbell", "Rodney Wallace", "Randall Azofeifa", "Francisco Calvo", "Cristian Gamboa", "Yeltsin Tejeda", "Patrick Pemberton", "Kendall Waston", "David Guzmán", "Marco Ureña", "Rónald Matarrita", "Leonel Moreira"], 
    
    "Serbia": ["Vladimir Stojković", "Antonio Rukavina", "Duško Tošić", "Luka Milivojević", "Uroš Spajić", "Branislav Ivanović", "Andrija Živković", "Aleksandar Prijović", "Aleksandar Mitrović", "Dušan Tadić", "Aleksandar Kolarov", "Predrag Rajković", "Miloš Veljković", "Milan Rodić", "Nikola Milenković", "Marko Grujić", "Filip Kostić", "Nemanja Radonjić", "Luka Jović", "Sergej Milinković-Savić", "Nemanja Matić", "Adem Ljajić", "Marko Dmitrović"], 
    
    "Switzerland": ["Yann Sommer", "Stephan Lichtsteiner", "François Moubandje", "Nico Elvedi", "Manuel Akanji", "Michael Lang", "Breel Embolo", "Remo Freuler", "Haris Seferović", "Granit Xhaka", "Valon Behrami", "Yvon Mvogo", "Ricardo Rodríguez", "Steven Zuber", "Blerim Džemaili", "Gelson Fernandes", "Denis Zakaria", "Mario Gavranović", "Josip Drmić", "Johan Djourou", "Roman Bürki", "Fabian Schär", "Xherdan Shaqiri"], 
    
    "Germany": ["Manuel Neuer", "Marvin Plattenhardt", "Jonas Hector", "Matthias Ginter", "Mats Hummels", "Sami Khedira", "Julian Draxler", "Toni Kroos", "Timo Werner", "Mesut Özil", "Marco Reus", "Kevin Trapp", "Thomas Müller", "Leon Goretzka", "Niklas Süle", "Antonio Rüdiger", "Jérôme Boateng", "Joshua Kimmich", "Sebastian Rudy", "Julian Brandt", "İlkay Gündoğan", "Marc-André ter Stegen", "Mario Gómez"], 
    
    "Mexico": ["José de Jesús Corona", "Hugo Ayala", "Carlos Salcedo", "Rafael Márquez", "Diego Reyes", "Jonathan dos Santos", "Miguel Layún", "Marco Fabián", "Raúl Jiménez", "Giovani dos Santos", "Carlos Vela", "Alfredo Talavera", "Guillermo Ochoa", "Javier Hernández", "Héctor Moreno", "Héctor Herrera", "Jesús Manuel Corona", "Andrés Guardado", "Oribe Peralta", "Javier Aquino", "Edson Álvarez", "Hirving Lozano", "Jesús Gallardo"], 
    
    "Korea Republic": ["Kim Seung-gyu", "Lee Yong", "Jung Seung-hyun", "Oh Ban-suk", "Yun Young-sun", "Park Joo-ho", "Son Heung-min", "Ju Se-jong", "Kim Shin-wook", "Lee Seung-woo", "Hwang Hee-chan", "Kim Min-woo", "Koo Ja-cheol", "Hong Chul", "Jung Woo-young", "Ki Sung-yueng", "Lee Jae-sung", "Moon Seon-min", "Kim Young-gwon", "Jang Hyun-soo", "Kim Jin-hyeon", "Go Yo-han", "Cho Hyun-woo"], 
    
    "Sweden": ["Robin Olsen", "Mikael Lustig", "Victor Lindelöf", "Andreas Granqvist", "Martin Olsson", "Ludwig Augustinsson", "Sebastian Larsson", "Albin Ekdal", "Marcus Berg", "Emil Forsberg", "John Guidetti", "Karl-Johan Johnsson", "Gustav Svensson", "Filip Helander", "Oscar Hiljemark", "Emil Krafth", "Viktor Claesson", "Pontus Jansson", "Marcus Rohdén", "Ola Toivonen", "Jimmy Durmaz", "Isaac Kiese Thelin", "Kristoffer Nordfeldt"], 
    
    "Belgium": ["Thibaut Courtois", "Toby Alderweireld", "Thomas Vermaelen", "Vincent Kompany", "Jan Vertonghen", "Axel Witsel", "Kevin De Bruyne", "Marouane Fellaini", "Romelu Lukaku", "Eden Hazard", "Yannick Carrasco", "Simon Mignolet", "Koen Casteels", "Dries Mertens", "Thomas Meunier", "Thorgan Hazard", "Youri Tielemans", "Adnan Januzaj", "Mousa Dembélé", "Dedryck Boyata", "Michy Batshuayi", "Nacer Chadli", "Leander Dendoncker"], 
    
    "England": ["Jordan Pickford", "Kyle Walker", "Danny Rose", "Eric Dier", "John Stones", "Harry Maguire", "Jesse Lingard", "Jordan Henderson", "Harry Kane", "Raheem Sterling", "Jamie Vardy", "Kieran Trippier", "Jack Butland", "Danny Welbeck", "Gary Cahill", "Phil Jones", "Fabian Delph", "Ashley Young", "Marcus Rashford", "Dele Alli", "Ruben Loftus-Cheek", "Trent Alexander-Arnold", "Nick Pope"], 
    
    "Panama": ["Jaime Penedo", "Michael Amir Murillo", "Harold Cummings", "Fidel Escobar", "Román Torres", "Gabriel Gómez", "Blas Pérez", "Édgar Bárcenas", "Gabriel Torres", "Ismael Díaz", "Armando Cooper", "José Calderón", "Adolfo Machado", "Valentín Pimentel", "Erick Davis", "Abdiel Arroyo", "Luis Ovalle", "Luis Tejada", "Ricardo Ávila", "Aníbal Godoy", "José Luis Rodríguez", "Álex Rodríguez", "Felipe Baloy"], 
    
    "Tunisia": ["Farouk Ben Mustapha", "Syam Ben Youssef", "Yohan Benalouane", "Yassine Meriah", "Oussama Haddadi", "Rami Bedoui", "Saîf-Eddine Khaoui", "Fakhreddine Ben Youssef", "Anice Badri", "Wahbi Khazri", "Dylan Bronn", "Ali Maâloul", "Ferjani Sassi", "Mohamed Amine Ben Amor", "Ahmed Khalil", "Aymen Mathlouthi", "Ellyes Skhiri", "Bassem Srarfi", "Saber Khalifa", "Ghailene Chaalali", "Hamdi Nagguez", "Mouez Hassen", "Naïm Sliti"], 
    
    "Colombia": ["David Ospina", "Cristián Zapata", "Óscar Murillo", "Santiago Arias", "Wílmar Barrios", "Carlos Sánchez", "Carlos Bacca", "Abel Aguilar", "Radamel Falcao", "James Rodríguez", "Juan Cuadrado", "Camilo Vargas", "Yerry Mina", "Luis Muriel", "Mateus Uribe", "Jefferson Lerma", "Johan Mojica", "Farid Díaz", "Miguel Borja", "Juan Fernando Quintero", "José Izquierdo", "José Fernando Cuadrado", "Dávinson Sánchez"], 
    
    "Japan": ["Eiji Kawashima", "Naomichi Ueda", "Gen Shoji", "Keisuke Honda", "Yuto Nagatomo", "Wataru Endo", "Gaku Shibasaki", "Genki Haraguchi", "Shinji Okazaki", "Shinji Kagawa", "Takashi Usami", "Masaaki Higashiguchi", "Yoshinori Mutō", "Takashi Inui", "Yuya Osako", "Hotaru Yamaguchi", "Makoto Hasebe", "Ryota Oshima", "Hiroki Sakai", "Tomoaki Makino", "Gōtoku Sakai", "Maya Yoshida", "Kosuke Nakamura"], 
    
    "Poland": ["Wojciech Szczęsny", "Michał Pazdan", "Artur Jędrzejczyk", "Thiago Cionek", "Jan Bednarek", "Jacek Góralski", "Arkadiusz Milik", "Karol Linetty", "Robert Lewandowski", "Grzegorz Krychowiak", "Kamil Grosicki", "Bartosz Białkowski", "Maciej Rybus", "Łukasz Teodorczyk", "Kamil Glik", "Jakub Błaszczykowski", "Sławomir Peszko", "Bartosz Bereszyński", "Piotr Zieliński", "Łukasz Piszczek", "Rafał Kurzawa", "Łukasz Fabiański", "Dawid Kownacki"], 
    
    "Senegal": ["Abdoulaye Diallo", "Saliou Ciss", "Kalidou Koulibaly", "Kara Mbodji", "Idrissa Gueye", "Salif Sané", "Moussa Sow", "Cheikhou Kouyaté", "Mame Biram Diouf", "Sadio Mané", "Cheikh N'Doye", "Youssouf Sabaly", "Alfred N'Diaye", "Moussa Konaté", "Diafra Sakho", "Khadim N'Diaye", "Badou Ndiaye", "Ismaïla Sarr", "M'Baye Niang", "Keita Baldé", "Lamine Gassama", "Moussa Wagué", "Alfred Gomis"]
}

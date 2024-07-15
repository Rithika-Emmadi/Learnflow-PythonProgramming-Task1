print("#######################################################################")
print("\n")
text = "WELCOME TO THE QUIZ"
print(text.center(50))
print("\n")

print("#######################################################################")


game_on = True
while game_on:
    questions = (
        (
            # General Knowledge Questions
            (  # Easy
                "What is the capital of France?",
                "What is the largest animal on Earth?",  
                "How many legs does a spider have?",  
                "Who was the first person to walk on the moon?",  
                "What color are bananas when they ripe?",  
            ),
            (  # Medium
                "What year did the Titanic sink?",  
                "What is the smallest country in the world?",
                "Who discovered penicillin?",  
                "Which planet is known as the Red Planet?",  
                "What is the longest river in the world?",  
            ),
            (  # Hard
                "What is the theory of relativity?",  
                "Who painted the Mona Lisa?",  
                "What is the main ingredient in sushi?",
                "Who wrote 'War and Peace'?",  
                "What is the capital of Iceland?",
            ),
        ),
        (
            # Basic CS Questions
            (  # Easy
                "What does CPU stand for?",  
                "What is the name of device used to point and click on the screen?",
                "What does HTML stand for?",  
                "What does www mean?",  
                "What is the main storage device in a computer called?",  
            ),
            (  # Medium
                "What is the first high-level programming language?",  
                "Who is known as the father of the computer?",
                "What is the main function of an operating system?",
                "What does RAM stand for?",  
                "What is the binary system?",  
            ),
            (  # Hard
                "What is the Turing Test?",  
                "What does TCP/IP stand for?",  
                "What is the difference between a compiler and an interpreter?",
                "What is polymorphism in OOP?",  
                "What is the time complexity of binary search?",
            ),
        ),
        (
            # Sports Questions
            (  # Easy
                "How many players are in a basketball team on the court at one time?",
                "In which sport do you perform a slam dunk?",  
                "How many bases are there in baseball?",  
                "In soccer, what card is shown to the player when sent off?",  
                "What is the national sport of India?",  
            ),
            (  # Medium
                "Who has won the most Olympic gold medals?",
                "What is the highest score in a single game in NBA history?",  
                "Which country has won the most World Cups in soccer?",  
                "Who holds the record for the fastest 100m sprint?",
                "What is the length of a marathon?",  
            ),
            (  # Hard
                "What is the Triple Crown in horse racing?",  
                "Who is the youngest player to score in the FIFA World Cup?",  
                "What is a perfect game in bowling?",  
                "What is the DRS system in cricket?",  
                "What is the diameter of a basketball hoop in inches?", 
            ),
        ),
        (
            # Social Knowledge Questions
            (  # Easy
                "What is the traditional dress worn by women in India?",
                "Who was the first Prime Minister of India?",  
                "When was World War fought?",
                "Name the country which was known as the country where sun never sets?",  
                "Name the company which ruled India?",  
            ),
            (  # Medium
                "What year did the Berlin Wall fall?",  
                "Who was the first president of the United States?",  
                "What is the most widely spoken language in the world?",
                "Who wrote 'The Communist Manifesto'?",  
                "What is the capital of Australia?",  
            ),
            (  # Hard
                "What is the significance of the Magna Carta?",  
                "Who was the longest-reigning British monarch?",  
                "What is the origin of the Olympic Games?",  
                "What is the primary function of the United Nations?",  
                "What is the highest court in the United States?",  
            ),
        ),
        (
            # Movies Questions
            (  # Easy
                "Which franchise has a character called Neville Longbottom?",
                "What does MCU stand for?",  
                "Which Telugu movie was nominated and won an Oscar?",  
                "Name the movie which tells the story of young Mark Zuckerberg?",
                "Name the actor who played as main lead in DUNE?",  
            ),
            (  # Medium
                "Who directed 'Inception'?",
                "Which movie won the first Academy Award for Best Picture?",
                "What is the highest-grossing film of all time?",
                "Who played Jack Dawson in 'Titanic'?",
                "What year was 'The Godfather' released?",
            ),
            (  # Hard
                "What is the plot of 'Pulp Fiction'?",
                "Who composed the score for 'Star Wars'?",
                "What is the significance of the Rosebud in 'Citizen Kane'?",
                "What is the longest movie ever made?",
                "What is the AFI's number one movie of all time?",
            ),
        ),
    )

    options = (
        (
            # General Knowledge Options
            (
                ("A. London", "B. Rome", "C. Paris", "D. Osaka"),
                ("A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Polar Bear"),
                ("A. Six", "B. Eight", "C. Ten", "D. Twelve"),
                ("A. Neil Armstrong", "B. Buzz Aldrin", "C. Yuri Gagarin", "D. John Glenn"),
                ("A. Red", "B. Green", "C. Purple", "D. Yellow"),
            ),
            (
                ("A. 1905", "B. 1912", "C. 1920", "D. 1931"),
                ("A. Monaco", "B. Vatican City", "C. San Marino", "D. Liechtenstein"),
                (
                    "A. Alexander Fleming",
                    "B. Louis Pasteur",
                    "C. Marie Curie",
                    "D. Gregor Mendel",
                ),
                ("A. Mars", "B. Jupiter", "C. Saturn", "D. Venus"),
                ("A. Amazon", "B. Nile", "C. Yangtze", "D. Mississippi"),
            ),
            (
                (
                    "A. Theory of Gravity",
                    "B. Quantum Mechanics",
                    "C. Theory of Relativity",
                    "D. String Theory",
                ),
                (
                    "A. Vincent van Gogh",
                    "B. Leonardo da Vinci",
                    "C. Pablo Picasso",
                    "D. Michelangelo",
                ),
                ("A. Rice", "B. Fish", "C. Seaweed", "D. Soy Sauce"),
                (
                    "A. Leo Tolstoy",
                    "B. Fyodor Dostoevsky",
                    "C. Jane Austen",
                    "D. Charles Dickens",
                ),
                ("A. Oslo", "B. Reykjavik", "C. Helsinki", "D. Copenhagen"),
            ),
        ),
        (
            # Basic CS Options
            (
                (
                    "A. Central Processing Unit",
                    "B. Central Process Unit",
                    "C. Computer Personal Unit",
                    "D. Central Processor Unit",
                ),
                ("A. Monitor", "B. Keyboard", "C. Mouse", "D. Printer"),
                (
                    "A. Hyper Text Markup Language",
                    "B. Hyperlinks and Text Markup Language",
                    "C. Home Tool Markup Language",
                    "D. Hyperlinking Text Marking Language",
                ),
                (
                    "A. World Wide Web",
                    "B. World Web Wide",
                    "C. Web Wide World",
                    "D. Wide World Web",
                ),
                ("A. RAM", "B. Hard Disk", "C. SSD", "D. CPU"),
            ),
            (
                ("A. COBOL", "B. FORTRAN", "C. BASIC", "D. Pascal"),
                (
                    "A. Alan Turing",
                    "B. Charles Babbage",
                    "C. John von Neumann",
                    "D. Ada Lovelace",
                ),
                (
                    "A. Managing software",
                    "B. Managing hardware",
                    "C. Managing resources",
                    "D. All of the above",
                ),
                (
                    "A. Random Access Memory",
                    "B. Read Access Memory",
                    "C. Run Access Memory",
                    "D. Real Access Memory",
                ),
                (
                    "A. A system of ones and zeros",
                    "B. A programming language",
                    "C. A software application",
                    "D. An algorithm",
                ),
            ),
            (
                (
                    "A. A test for artificial intelligence",
                    "B. A test for quantum computers",
                    "C. A test for computer speed",
                    "D. A test for software bugs",
                ),
                (
                    "A. Transmission Control Protocol/Internet Protocol",
                    "B. Transfer Control Protocol/Internet Protocol",
                    "C. Transmission Control Protocol/Interface Protocol",
                    "D. Transfer Control Protocol/Interface Protocol",
                ),
                (
                    "A. A compiler translates code all at once, while an interpreter translates code line by line",
                    "B. An interpreter translates code all at once, while a compiler translates code line by line",
                    "C. Both translate code all at once",
                    "D. Both translate code line by line",
                ),
                (
                    "A. The ability of different classes to be treated as instances of the same class",
                    "B. The ability of a function to return multiple values",
                    "C. The ability of a class to inherit from multiple classes",
                    "D. The ability of a variable to change type",
                ),
                ("A. O(log n)", "B. O(n)", "C. O(n log n)", "D. O(1)"),
            ),
        ),
        (
            # Sports Options
            (
                ("A. Five", "B. Six", "C. Seven", "D. Eight"),
                ("A. Soccer", "B. Basketball", "C. Tennis", "D. Football"),
                ("A. Two", "B. Three", "C. Four", "D. Five"),
                ("A. Red Card", "B. Yellow Card", "C. Green Card", "D. Blue Card"),
                ("A. Cricket", "B. Hockey", "C. Kabaddi", "D. Football"),
            ),
            (
                (
                    "A. Michael Phelps",
                    "B. Usain Bolt",
                    "C. Carl Lewis",
                    "D. Larisa Latynina",
                ),
                ("A. 100 points", "B. 81 points", "C. 71 points", "D. 93 points"),
                ("A. Germany", "B. Argentina", "C. Brazil", "D. Italy"),
                ("A. Carl Lewis", "B. Maurice Greene", "C. Usain Bolt", "D. Yohan Blake"),
                ("A. 42.195 km", "B. 40.195 km", "C. 45.195 km", "D. 50.195 km"),
            ),
            (
                (
                    "A. Winning the Kentucky Derby, Preakness Stakes, and Belmont Stakes",
                    "B. Winning three Grand Slam tournaments in one year",
                    "C. Scoring three goals in one game",
                    "D. Winning three Olympic gold medals in one event",
                ),
                ("A. Pele", "B. Diego Maradona", "C. Lionel Messi", "D. Kylian Mbappe"),
                (
                    "A. Scoring a strike in every frame",
                    "B. Bowling a perfect 300",
                    "C. Bowling three strikes in a row",
                    "D. Knocking down all pins with one ball",
                ),
                (
                    "A. Decision Review System",
                    "B. Digital Replay System",
                    "C. Dynamic Review System",
                    "D. Direct Replay System",
                ),
                ("A. 15 inches", "B. 16 inches", "C. 17 inches", "D. 18 inches"),
            ),
        ),
        (
            # Social Knowledge Options
            (
                ("A. Saree", "B. Kimono", "C. Hanbok", "D. Cheongsam"),
                (
                    "A. Indira Gandhi",
                    "B. Jawaharlal Nehru",
                    "C. Mahatma Gandhi",
                    "D. Rajiv Gandhi",
                ),
                ("A. 1914-1918", "B. 1939-1945", "C. 1917-1921", "D. 1941-1945"),
                ("A. France", "B. England", "C. Spain", "D. Russia"),
                (
                    "A. British East India Company",
                    "B. Dutch East India Company",
                    "C. French East India Company",
                    "D. Portuguese East India Company",
                ),
            ),
            (
                ("A. 1989", "B. 1991", "C. 1985", "D. 1993"),
                (
                    "A. George Washington",
                    "B. Thomas Jefferson",
                    "C. John Adams",
                    "D. James Madison",
                ),
                ("A. English", "B. Spanish", "C. Mandarin", "D. Hindi"),
                (
                    "A. Karl Marx and Friedrich Engels",
                    "B. Vladimir Lenin",
                    "C. Joseph Stalin",
                    "D. Mao Zedong",
                ),
                ("A. Sydney", "B. Melbourne", "C. Canberra", "D. Perth"),
            ),
            (
                (
                    "A. The first document to limit the power of the king",
                    "B. The foundation of modern democracy",
                    "C. The declaration of independence of England",
                    "D. The first constitution of the United States",
                ),
                (
                    "A. Queen Victoria",
                    "B. Queen Elizabeth I",
                    "C. Queen Elizabeth II",
                    "D. King George III",
                ),
                ("A. Greece", "B. Rome", "C. Egypt", "D. China"),
                (
                    "A. To maintain international peace and security",
                    "B. To promote economic growth",
                    "C. To develop space technology",
                    "D. To regulate global trade",
                ),
                (
                    "A. The Supreme Court",
                    "B. The High Court",
                    "C. The Appellate Court",
                    "D. The Federal Court",
                ),
            ),
        ),
        (
            # Movies Options
            (
                (
                    "A. Hunger Games",
                    "B. Lord of the Rings",
                    "C. Star Wars",
                    "D. Harry Potter",
                ),
                (
                    "A. Magic Cinematic Universe",
                    "B. Monster Cinematic Universe",
                    "C. Marvel Cinematic Universe",
                    "D. Machine Cinematic Universe",
                ),
                ("A. Baahubali", "B. RRR", "C. Pushpa", "D. KGF"),
                (
                    "A. The Social Network",
                    "B. The Facebook Story",
                    "C. The Zuck Life",
                    "D. The Internet Giant",
                ),
                (
                    "A. Tom Holland",
                    "B. Chris Pratt",
                    "C. Robert Pattinson",
                    "D. Timothée Chalamet",
                ),
            ),
            (
                (
                    "A. Christopher Nolan",
                    "B. Steven Spielberg",
                    "C. James Cameron",
                    "D. Quentin Tarantino",
                ),
                (
                    "A. Wings",
                    "B. Sunrise",
                    "C. The Broadway Melody",
                    "D. All Quiet on the Western Front",
                ),
                (
                    "A. Avatar",
                    "B. Avengers: Endgame",
                    "C. Titanic",
                    "D. Star Wars: The Force Awakens",
                ),
                ("A. Leonardo DiCaprio", "B. Brad Pitt", "C. Johnny Depp", "D. Matt Damon"),
                ("A. 1970", "B. 1972", "C. 1974", "D. 1976"),
            ),
            (
                (
                    "A. A non-linear narrative following different characters",
                    "B. A story about a boxer",
                    "C. A heist movie",
                    "D. A war movie",
                ),
                (
                    "A. Hans Zimmer",
                    "B. John Williams",
                    "C. Howard Shore",
                    "D. Ennio Morricone",
                ),
                ("A. A rosebud", "B. A sled", "C. A painting", "D. A diary"),
                ("A. The Cure for Insomnia", "B. Out 1", "C. Ambiancé", "D. Resan"),
                (
                    "A. Gone with the Wind",
                    "B. The Godfather",
                    "C. Casablanca",
                    "D. Citizen Kane",
                ),
            ),
        ),
    )

    answers = (
        (  # GK
            ("C", "B", "B", "A", "D"),  # Easy
            ("B", "B", "A", "A", "B"),  # Medium
            ("C", "B", "A", "A", "B"),  # Hard
        ),
        (  # Basic CS
            ("A", "C", "A", "A", "B"),  # Easy
            ("B", "B", "D", "A", "A"),  # Medium
            ("A", "A", "A", "A", "A"),  # Hard
        ),
        (  # Sports
            ("B", "B", "C", "A", "B"),  # Easy
            ("A", "A", "C", "C", "A"),  # Medium
            ("A", "D", "B", "A", "D"),  # Hard
        ),
        (  # Social Knowledge
            ("A", "B", "B", "B", "A"),  # Easy
            ("A", "A", "C", "A", "C"),  # Medium
            ("A", "C", "A", "A", "A"),  # Hard
        ),
        (  # Movies
            ("D", "C", "B", "A", "D"),  # Easy
            ("A", "A", "B", "A", "B"),  # Medium
            ("A", "B", "B", "A", "D"),  # Hard
        ),
    )

    print("The topics are\n")
    print(
        "A. General Knowledge\nB. Basics in CS\nC. Sports\nD. Social Knowledge\nE. Movies\n"
    )
    chosen_topic = input("Choose any one topic\n").upper()

    topic_number = -1
    if chosen_topic == "A":
        topic_number = 0
    elif chosen_topic == "B":
        topic_number = 1
    elif chosen_topic == "C":
        topic_number = 2
    elif chosen_topic == "D":
        topic_number = 3
    elif chosen_topic == "E":
        topic_number = 4
    else:
        print("Invalid topic chosen.")
        exit()

    print("Which level of difficulty would you like to play?")
    print("A. Easy\nB. Medium\nC. Hard\n")
    chosen_level = input("Enter your choice:").upper()

    diff_level = -1
    if chosen_level == "A":
        diff_level = 0
    elif chosen_level == "B":
        diff_level = 1
    elif chosen_level == "C":
        diff_level = 2
    else:
        print("Invalid option")
        exit()

    guess = []

    for i in range(0, 5):
        print(questions[topic_number][diff_level][i])

        for option in options[topic_number][diff_level][i]:
            print(option)
        print("\n")
        guess.append(input("Your choice:\n").upper())

    score = 0
    for i in range(0, 5):
        if guess[i] == answers[topic_number][diff_level][i]:
            score += 1

    print("Your answers were:")
    for i in range(0, 5):
        print(guess[i])
    print("\n")
    print("Correct answers are:")
    for i in range(0, 5):
        print(answers[topic_number][diff_level][i])
    print("\n")
    print(f"Hence, your score is:\n{score}")
    if score == 0:
        print("Better luck next time!")
    elif score > 0 and score <= 3:
        print("You can do better")
    else:
        print("You did fantastic!")

    check = input("Do you want to play again? (Y/n)")
    if check == 'n':
        game_on = False

print("Exiting the game...")
exit()

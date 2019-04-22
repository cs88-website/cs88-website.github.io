-- Comment out the unfinished questions while you
-- are working so as to avoid errors in the tests.

-- Scroll past the tables to reach the questions you
-- will be answering.

create table artists as
	select 1 as artistID, 'AC/DC' as name union
	select 2, 'Accept' union
	select 3, 'Aerosmith' union
	select 4, 'Alanis Morissette' union
	select 5, 'Alice In Chains' union
	select 6, 'Antonio Carlos Jobim' union
	select 7, 'Apocalyptica' union
	select 8, 'Audioslave' union
	select 9, 'BackBeat' union
	select 10, 'Billy Cobham' union
	select 11, 'Black Label Society' union
	select 12, 'Black Sabbath' union
	select 13, 'Body Count' union
	select 14, 'Bruce Dickinson' union
	select 15, 'Buddy Guy' union
	select 16, 'Caetano Veloso' union
	select 17, 'Chico Buarque' union
	select 18, 'Chico Science & Nacao Zumbi' union
	select 19, 'Cidade Negra' union
	select 20, 'Claudio Zoli' union
	select 21, 'Various Artists' union
	select 22, 'Led Zeppelin' union
	select 23, 'Frank Zappa & Captain Beefheart' union
	select 24, 'Marcos Valle' union
	select 25, 'Milton Nascimento & Bebeto' union
	select 26, 'Azymuth' union
	select 27, 'Gilberto Gil' union
	select 28, 'Joao Gilberto' union
	select 29, 'Bebel Gilberto' union
	select 30, 'Jorge Vercilo' union
	select 31, 'Baby Consuelo' union
	select 32, 'Ney Matogrosso' union
	select 33, 'Luiz Melodia' union
	select 34, 'Nando Reis' union
	select 35, 'Pedro Luis & A Parede' union
	select 36, 'O Rappa' union
	select 37, 'Ed Motta' union
	select 38, 'Banda Black Rio' union
	select 39, 'Fernanda Porto' union
	select 40, 'Os Cariocas' union
	select 41, 'Elis Regina' union
	select 42, 'Milton Nascimento' union
	select 43, 'A Cor Do Som' union
	select 44, 'Kid Abelha' union
	select 45, 'Sandra De Sa' union
	select 46, 'Jorge Ben' union
	select 47, 'Hermeto Pascoal' union
	select 48, 'Barao Vermelho' union
	select 49, 'Edson, DJ Marky & DJ Patife Featuring Fernanda Porto' union
	select 50, 'Metallica' union
	select 51, 'Queen' union
	select 52, 'Kiss' union
	select 53, 'Spyro Gyra' union
	select 54, 'Green Day' union
	select 55, 'David Coverdale' union
	select 56, 'Gonzaguinha' union
	select 57, 'Os Mutantes' union
	select 58, 'Deep Purple' union
	select 59, 'Santana' union
	select 60, 'Santana Feat. Dave Matthews' union
	select 61, 'Santana Feat. Everlast' union
	select 62, 'Santana Feat. Rob Thomas' union
	select 63, 'Santana Feat. Lauryn Hill & Cee-Lo' union
	select 64, 'Santana Feat. The Project G&B' union
	select 65, 'Santana Feat. Mana' union
	select 66, 'Santana Feat. Eagle-Eye Cherry' union
	select 67, 'Santana Feat. Eric Clapton' union
	select 68, 'Miles Davis' union
	select 69, 'Gene Krupa' union
	select 70, 'Toquinho & Vinicius' union
	select 71, 'Vinicius De Moraes & Baden Powell' union
	select 72, 'Vinicius De Moraes' union
	select 73, 'Vinicius E Qurteto Em Cy' union
	select 74, 'Vinicius E Odette Lara' union
	select 75, 'Vinicius, Toquinho & Quarteto Em Cy' union
	select 76, 'Creedence Clearwater Revival' union
	select 77, 'Cassia Eller' union
	select 78, 'Def Leppard' union
	select 79, 'Dennis Chambers' union
	select 80, 'Djavan' union
	select 81, 'Eric Clapton' union
	select 82, 'Faith No More' union
	select 83, 'Falamansa' union
	select 84, 'Foo Fighters' union
	select 85, 'Frank Sinatra' union
	select 86, 'Funk Como Le Gusta' union
	select 87, 'Godsmack' union
	select 88, 'Guns N'' Roses' union
	select 89, 'Incognito' union
	select 90, 'Iron Maiden' union
	select 91, 'James Brown' union
	select 92, 'Jamiroquai' union
	select 93, 'JET' union
	select 94, 'Jimi Hendrix' union
	select 95, 'Joe Satriani' union
	select 96, 'Jota Quest' union
	select 97, 'Joao Suplicy' union
	select 98, 'Judas Priest' union
	select 99, 'Legiao Urbana' union
	select 100, 'Lenny Kravitz' union
	select 101, 'Lulu Santos' union
	select 102, 'Marillion' union
	select 103, 'Marisa Monte' union
	select 104, 'Marvin Gaye' union
	select 105, 'Men At Work' union
	select 106, 'Motorhead' union
	select 107, 'Motorhead & Girlschool' union
	select 108, 'Monica Marianno' union
	select 109, 'Motley Crue' union
	select 110, 'Nirvana' union
	select 111, 'O Terco' union
	select 112, 'Olodum' union
	select 113, 'Os Paralamas Do Sucesso' union
	select 114, 'Ozzy Osbourne' union
	select 115, 'Page & Plant' union
	select 116, 'Passengers' union
	select 117, 'Paul D''Ianno' union
	select 118, 'Pearl Jam' union
	select 119, 'Peter Tosh' union
	select 120, 'Pink Floyd' union
	select 121, 'Planet Hemp' union
	select 122, 'R.E.M. Feat. Kate Pearson' union
	select 123, 'R.E.M. Feat. KRS-One' union
	select 124, 'R.E.M.' union
	select 125, 'Raimundos' union
	select 126, 'Raul Seixas' union
	select 127, 'Red Hot Chili Peppers' union
	select 128, 'Rush' union
	select 129, 'Simply Red' union
	select 130, 'Skank' union
	select 131, 'Smashing Pumpkins' union
	select 132, 'Soundgarden' union
	select 133, 'Stevie Ray Vaughan & Double Trouble' union
	select 134, 'Stone Temple Pilots' union
	select 135, 'System Of A Down' union
	select 136, 'Terry Bozzio, Tony Levin & Steve Stevens' union
	select 137, 'The Black Crowes' union
	select 138, 'The Clash' union
	select 139, 'The Cult' union
	select 140, 'The Doors' union
	select 141, 'The Police' union
	select 142, 'The Rolling Stones' union
	select 143, 'The Tea Party' union
	select 144, 'The Who' union
	select 145, 'Tim Maia' union
	select 146, 'Titas' union
	select 147, 'Battlestar Galactica' union
	select 148, 'Heroes' union
	select 149, 'Lost' union
	select 150, 'U2' union
	select 151, 'UB40' union
	select 152, 'Van Halen' union
	select 153, 'Velvet Revolver' union
	select 154, 'Whitesnake' union
	select 155, 'Zeca Pagodinho' union
	select 156, 'The Office' union
	select 157, 'Dread Zeppelin' union
	select 158, 'Battlestar Galactica (Classic)' union
	select 159, 'Aquaman' union
	select 160, 'Christina Aguilera featuring BigElf' union
	select 161, 'Aerosmith & Sierra Leone''s Refugee Allstars' union
	select 162, 'Los Lonely Boys' union
	select 163, 'Corinne Bailey Rae' union
	select 164, 'Dhani Harrison & Jakob Dylan' union
	select 165, 'Jackson Browne' union
	select 166, 'Avril Lavigne' union
	select 167, 'Big & Rich' union
	select 168, 'Youssou N''Dour' union
	select 169, 'Black Eyed Peas' union
	select 170, 'Jack Johnson' union
	select 171, 'Ben Harper' union
	select 172, 'Snow Patrol' union
	select 173, 'Matisyahu' union
	select 174, 'The Postal Service' union
	select 175, 'Jaguares' union
	select 176, 'The Flaming Lips' union
	select 177, 'Jack''s Mannequin & Mick Fleetwood' union
	select 178, 'Regina Spektor' union
	select 179, 'Scorpions' union
	select 180, 'House Of Pain' union
	select 181, 'Xis' union
	select 182, 'Nega Gizza' union
	select 183, 'Gustavo & Andres Veiga & Salazar' union
	select 184, 'Rodox' union
	select 185, 'Charlie Brown Jr.' union
	select 186, 'Pedro Luis E A Parede' union
	select 187, 'Los Hermanos' union
	select 188, 'Mundo Livre S/A' union
	select 189, 'Otto' union
	select 190, 'Instituto' union
	select 191, 'Nacao Zumbi' union
	select 192, 'DJ Dolores & Orchestra Santa Massa' union
	select 193, 'Seu Jorge' union
	select 194, 'Sabotage E Instituto' union
	select 195, 'Stereo Maracana' union
	select 196, 'Cake' union
	select 197, 'Aisha Duo' union
	select 198, 'Habib Koite and Bamada' union
	select 199, 'Karsh Kale' union
	select 200, 'The Posies' union
	select 201, 'Luciana Souza/Romero Lubambo' union
	select 202, 'Aaron Goldberg' union
	select 203, 'Nicolaus Esterhazy Sinfonia' union
	select 204, 'Temple of the Dog' union
	select 205, 'Chris Cornell' union
	select 206, 'Alberto Turco & Nova Schola Gregoriana' union
	select 207, 'Richard Marlow & The Choir of Trinity College, Cambridge' union
	select 208, 'English Concert & Trevor Pinnock' union
	select 209, 'Anne-Sophie Mutter, Herbert Von Karajan & Wiener Philharmoniker' union
	select 210, 'Hilary Hahn, Jeffrey Kahane, Los Angeles Chamber Orchestra & Margaret Batjer' union
	select 211, 'Wilhelm Kempff' union
	select 212, 'Yo-Yo Ma' union
	select 213, 'Scholars Baroque Ensemble' union
	select 214, 'Academy of St. Martin in the Fields & Sir Neville Marriner' union
	select 215, 'Academy of St. Martin in the Fields Chamber Ensemble & Sir Neville Marriner' union
	select 216, 'Berliner Philharmoniker, Claudio Abbado & Sabine Meyer' union
	select 217, 'Royal Philharmonic Orchestra & Sir Thomas Beecham' union
	select 218, 'Orchestre Revolutionnaire et Romantique & John Eliot Gardiner' union
	select 219, 'Britten Sinfonia, Ivor Bolton & Lesley Garrett' union
	select 220, 'Chicago Symphony Chorus, Chicago Symphony Orchestra & Sir Georg Solti' union
	select 221, 'Sir Georg Solti & Wiener Philharmoniker' union
	select 222, 'Academy of St. Martin in the Fields, John Birch, Sir Neville Marriner & Sylvia McNair' union
	select 223, 'London Symphony Orchestra & Sir Charles Mackerras' union
	select 224, 'Barry Wordsworth & BBC Concert Orchestra' union
	select 225, 'Herbert Von Karajan, Mirella Freni & Wiener Philharmoniker' union
	select 226, 'Eugene Ormandy' union
	select 227, 'Luciano Pavarotti' union
	select 228, 'Leonard Bernstein & New York Philharmonic' union
	select 229, 'Boston Symphony Orchestra & Seiji Ozawa' union
	select 230, 'Aaron Copland & London Symphony Orchestra' union
	select 231, 'Ton Koopman' union
	select 232, 'Sergei Prokofiev & Yuri Temirkanov' union
	select 233, 'Chicago Symphony Orchestra & Fritz Reiner' union
	select 234, 'Orchestra of The Age of Enlightenment' union
	select 235, 'Emanuel Ax, Eugene Ormandy & Philadelphia Orchestra' union
	select 236, 'James Levine' union
	select 237, 'Berliner Philharmoniker & Hans Rosbaud' union
	select 238, 'Maurizio Pollini' union
	select 239, 'Academy of St. Martin in the Fields, Sir Neville Marriner & William Bennett' union
	select 240, 'Gustav Mahler' union
	select 241, 'Felix Schmidt, London Symphony Orchestra & Rafael Fruhbeck de Burgos' union
	select 242, 'Edo de Waart & San Francisco Symphony' union
	select 243, 'Antal Dorati & London Symphony Orchestra' union
	select 244, 'Choir Of Westminster Abbey & Simon Preston' union
	select 245, 'Michael Tilson Thomas & San Francisco Symphony' union
	select 246, 'Chor der Wiener Staatsoper, Herbert Von Karajan & Wiener Philharmoniker' union
	select 247, 'The King''s Singers' union
	select 248, 'Berliner Philharmoniker & Herbert Von Karajan' union
	select 249, 'Sir Georg Solti, Sumi Jo & Wiener Philharmoniker' union
	select 250, 'Christopher O''Riley' union
	select 251, 'Fretwork' union
	select 252, 'Amy Winehouse' union
	select 253, 'Calexico' union
	select 254, 'Otto Klemperer & Philharmonia Orchestra' union
	select 255, 'Yehudi Menuhin' union
	select 256, 'Philharmonia Orchestra & Sir Neville Marriner' union
	select 257, 'Academy of St. Martin in the Fields, Sir Neville Marriner & Thurston Dart' union
	select 258, 'Les Arts Florissants & William Christie' union
	select 259, 'The 12 Cellists of The Berlin Philharmonic' union
	select 260, 'Adrian Leaper & Doreen de Feis' union
	select 261, 'Roger Norrington, London Classical Players' union
	select 262, 'Charles Dutoit & L''Orchestre Symphonique de Montreal' union
	select 263, 'Equale Brass Ensemble, John Eliot Gardiner & Munich Monteverdi Orchestra and Choir' union
	select 264, 'Kent Nagano and Orchestre de l''Opera de Lyon' union
	select 265, 'Julian Bream' union
	select 266, 'Martin Roscoe' union
	select 267, 'Goteborgs Symfoniker & Neeme Jarvi' union
	select 268, 'Itzhak Perlman' union
	select 269, 'Michele Campanella' union
	select 270, 'Gerald Moore' union
	select 271, 'Mela Tenenbaum, Pro Musica Prague & Richard Kapp' union
	select 272, 'Emerson String Quartet' union
	select 273, 'C. Monteverdi, Nigel Rogers - Chiaroscuro; London Baroque; London Cornett & Sackbu' union
	select 274, 'Nash Ensemble' union
	select 275, 'Philip Glass Ensemble';

create table albums as
	select 1 as albumID, 'For Those About To Rock We Salute You' as title, 1 as artistID union
	select 2, 'Balls to the Wall', 2 union
	select 3, 'Restless and Wild', 2 union
	select 4, 'Let There Be Rock', 1 union
	select 5, 'Big Ones', 3 union
	select 6, 'Jagged Little Pill', 4 union
	select 7, 'Facelift', 5 union
	select 8, 'Warner 25 Anos', 6 union
	select 9, 'Plays Metallica By Four Cellos', 7 union
	select 10, 'Audioslave', 8 union
	select 11, 'Out Of Exile', 8 union
	select 12, 'BackBeat Soundtrack', 9 union
	select 13, 'The Best Of Billy Cobham', 10 union
	select 14, 'Alcohol Fueled Brewtality Live! [Disc 1]', 11 union
	select 15, 'Alcohol Fueled Brewtality Live! [Disc 2]', 11 union
	select 16, 'Black Sabbath', 12 union
	select 17, 'Black Sabbath Vol. 4 (Remaster)', 12 union
	select 18, 'Body Count', 13 union
	select 19, 'Chemical Wedding', 14 union
	select 20, 'The Best Of Buddy Guy - The Millenium Collection', 15 union
	select 21, 'Prenda Minha', 16 union
	select 22, 'Sozinho Remix Ao Vivo', 16 union
	select 23, 'Minha Historia', 17 union
	select 24, 'Afrociberdelia', 18 union
	select 25, 'Da Lama Ao Caos', 18 union
	select 26, 'Acustico MTV [Live]', 19 union
	select 27, 'Cidade Negra - Hits', 19 union
	select 28, 'Na Pista', 20 union
	select 29, 'Axe Bahia 2001', 21 union
	select 30, 'BBC Sessions [Disc 1] [Live]', 22 union
	select 31, 'Bongo Fury', 23 union
	select 32, 'Carnaval 2001', 21 union
	select 33, 'Chill: Brazil (Disc 1)', 24 union
	select 34, 'Chill: Brazil (Disc 2)', 6 union
	select 35, 'Garage Inc. (Disc 1)', 50 union
	select 36, 'Greatest Hits II', 51 union
	select 37, 'Greatest Kiss', 52 union
	select 38, 'Heart of the Night', 53 union
	select 39, 'International Superhits', 54 union
	select 40, 'Into The Light', 55 union
	select 41, 'Meus Momentos', 56 union
	select 42, 'Minha Historia', 57 union
	select 43, 'MK III The Final Concerts [Disc 1]', 58 union
	select 44, 'Physical Graffiti [Disc 1]', 22 union
	select 45, 'Sambas De Enredo 2001', 21 union
	select 46, 'Supernatural', 59 union
	select 47, 'The Best of Ed Motta', 37 union
	select 48, 'The Essential Miles Davis [Disc 1]', 68 union
	select 49, 'The Essential Miles Davis [Disc 2]', 68 union
	select 50, 'The Final Concerts (Disc 2)', 58 union
	select 51, 'Up An'' Atom', 69 union
	select 52, 'Vinicius De Moraes - Sem Limite', 70 union
	select 53, 'Vozes do MPB', 21 union
	select 54, 'Chronicle, Vol. 1', 76 union
	select 55, 'Chronicle, Vol. 2', 76 union
	select 56, 'Cassia Eller - Colecao Sem Limite [Disc 2]', 77 union
	select 57, 'Cassia Eller - Sem Limite [Disc 1]', 77 union
	select 58, 'Come Taste The Band', 58 union
	select 59, 'Deep Purple In Rock', 58 union
	select 60, 'Fireball', 58 union
	select 61, 'Knocking at Your Back Door: The Best Of Deep Purple in the 80''s', 58 union
	select 62, 'Machine Head', 58 union
	select 63, 'Purpendicular', 58 union
	select 64, 'Slaves And Masters', 58 union
	select 65, 'Stormbringer', 58 union
	select 66, 'The Battle Rages On', 58 union
	select 67, 'Vault: Def Leppard''s Greatest Hits', 78 union
	select 68, 'Outbreak', 79 union
	select 69, 'Djavan Ao Vivo - Vol. 02', 80 union
	select 70, 'Djavan Ao Vivo - Vol. 1', 80 union
	select 71, 'Elis Regina-Minha Historia', 41 union
	select 72, 'The Cream Of Clapton', 81 union
	select 73, 'Unplugged', 81 union
	select 74, 'Album Of The Year', 82 union
	select 75, 'Angel Dust', 82 union
	select 76, 'King For A Day Fool For A Lifetime', 82 union
	select 77, 'The Real Thing', 82 union
	select 78, 'Deixa Entrar', 83 union
	select 79, 'In Your Honor [Disc 1]', 84 union
	select 80, 'In Your Honor [Disc 2]', 84 union
	select 81, 'One By One', 84 union
	select 82, 'The Colour And The Shape', 84 union
	select 83, 'My Way: The Best Of Frank Sinatra [Disc 1]', 85 union
	select 84, 'Roda De Funk', 86 union
	select 85, 'As Cancoes de Eu Tu Eles', 27 union
	select 86, 'Quanta Gente Veio Ver (Live)', 27 union
	select 87, 'Quanta Gente Veio ver--Bonus De Carnaval', 27 union
	select 88, 'Faceless', 87 union
	select 89, 'American Idiot', 54 union
	select 90, 'Appetite for Destruction', 88 union
	select 91, 'Use Your Illusion I', 88 union
	select 92, 'Use Your Illusion II', 88 union
	select 93, 'Blue Moods', 89 union
	select 94, 'A Matter of Life and Death', 90 union
	select 95, 'A Real Dead One', 90 union
	select 96, 'A Real Live One', 90 union
	select 97, 'Brave New World', 90 union
	select 98, 'Dance Of Death', 90 union
	select 99, 'Fear Of The Dark', 90 union
	select 100, 'Iron Maiden', 90 union
	select 101, 'Killers', 90 union
	select 102, 'Live After Death', 90 union
	select 103, 'Live At Donington 1992 (Disc 1)', 90 union
	select 104, 'Live At Donington 1992 (Disc 2)', 90 union
	select 105, 'No Prayer For The Dying', 90 union
	select 106, 'Piece Of Mind', 90 union
	select 107, 'Powerslave', 90 union
	select 108, 'Rock In Rio [CD1]', 90 union
	select 109, 'Rock In Rio [CD2]', 90 union
	select 110, 'Seventh Son of a Seventh Son', 90 union
	select 111, 'Somewhere in Time', 90 union
	select 112, 'The Number of The Beast', 90 union
	select 113, 'The X Factor', 90 union
	select 114, 'Virtual XI', 90 union
	select 115, 'Sex Machine', 91 union
	select 116, 'Emergency On Planet Earth', 92 union
	select 117, 'Synkronized', 92 union
	select 118, 'The Return Of The Space Cowboy', 92 union
	select 119, 'Get Born', 93 union
	select 120, 'Are You Experienced?', 94 union
	select 121, 'Surfing with the Alien (Remastered)', 95 union
	select 122, 'Jorge Ben Jor 25 Anos', 46 union
	select 123, 'Jota Quest-1995', 96 union
	select 124, 'Cafezinho', 97 union
	select 125, 'Living After Midnight', 98 union
	select 126, 'Unplugged [Live]', 52 union
	select 127, 'BBC Sessions [Disc 2] [Live]', 22 union
	select 128, 'Coda', 22 union
	select 129, 'Houses Of The Holy', 22 union
	select 130, 'In Through The Out Door', 22 union
	select 131, 'IV', 22 union
	select 132, 'Led Zeppelin I', 22 union
	select 133, 'Led Zeppelin II', 22 union
	select 134, 'Led Zeppelin III', 22 union
	select 135, 'Physical Graffiti [Disc 2]', 22 union
	select 136, 'Presence', 22 union
	select 137, 'The Song Remains The Same (Disc 1)', 22 union
	select 138, 'The Song Remains The Same (Disc 2)', 22 union
	select 139, 'A TempestadeTempestade Ou O Livro Dos Dias', 99 union
	select 140, 'Mais Do Mesmo', 99 union
	select 141, 'Greatest Hits', 100 union
	select 142, 'Lulu Santos - RCA 100 Anos De Musica - Album 01', 101 union
	select 143, 'Lulu Santos - RCA 100 Anos De Musica - Album 02', 101 union
	select 144, 'Misplaced Childhood', 102 union
	select 145, 'Barulhinho Bom', 103 union
	select 146, 'Seek And Shall Find: More Of The Best (1963-1981)', 104 union
	select 147, 'The Best Of Men At Work', 105 union
	select 148, 'Black Album', 50 union
	select 149, 'Garage Inc. (Disc 2)', 50 union
	select 150, 'Kill ''Em All', 50 union
	select 151, 'Load', 50 union
	select 152, 'Master Of Puppets', 50 union
	select 153, 'ReLoad', 50 union
	select 154, 'Ride The Lightning', 50 union
	select 155, 'St. Anger', 50 union
	select 156, '...And Justice For All', 50 union
	select 157, 'Miles Ahead', 68 union
	select 158, 'Milton Nascimento Ao Vivo', 42 union
	select 159, 'Minas', 42 union
	select 160, 'Ace Of Spades', 106 union
	select 161, 'Demorou...', 108 union
	select 162, 'Motley Crue Greatest Hits', 109 union
	select 163, 'From The Muddy Banks Of The Wishkah [Live]', 110 union
	select 164, 'Nevermind', 110 union
	select 165, 'Compositores', 111 union
	select 166, 'Olodum', 112 union
	select 167, 'Acustico MTV', 113 union
	select 168, 'Arquivo II', 113 union
	select 169, 'Arquivo Os Paralamas Do Sucesso', 113 union
	select 170, 'Bark at the Moon (Remastered)', 114 union
	select 171, 'Blizzard of Ozz', 114 union
	select 172, 'Diary of a Madman (Remastered)', 114 union
	select 173, 'No More Tears (Remastered)', 114 union
	select 174, 'Tribute', 114 union
	select 175, 'Walking Into Clarksdale', 115 union
	select 176, 'Original Soundtracks 1', 116 union
	select 177, 'The Beast Live', 117 union
	select 178, 'Live On Two Legs [Live]', 118 union
	select 179, 'Pearl Jam', 118 union
	select 180, 'Riot Act', 118 union
	select 181, 'Ten', 118 union
	select 182, 'Vs.', 118 union
	select 183, 'Dark Side Of The Moon', 120 union
	select 184, 'Os Caes Ladram Mas A Caravana Nao Para', 121 union
	select 185, 'Greatest Hits I', 51 union
	select 186, 'News Of The World', 51 union
	select 187, 'Out Of Time', 122 union
	select 188, 'Green', 124 union
	select 189, 'New Adventures In Hi-Fi', 124 union
	select 190, 'The Best Of R.E.M.: The IRS Years', 124 union
	select 191, 'Cesta Basica', 125 union
	select 192, 'Raul Seixas', 126 union
	select 193, 'Blood Sugar Sex Magik', 127 union
	select 194, 'By The Way', 127 union
	select 195, 'Californication', 127 union
	select 196, 'Retrospective I (1974-1980)', 128 union
	select 197, 'Santana - As Years Go By', 59 union
	select 198, 'Santana Live', 59 union
	select 199, 'Maquinarama', 130 union
	select 200, 'O Samba Pocone', 130 union
	select 201, 'Judas 0: B-Sides and Rarities', 131 union
	select 202, 'Rotten Apples: Greatest Hits', 131 union
	select 203, 'A-Sides', 132 union
	select 204, 'Morning Dance', 53 union
	select 205, 'In Step', 133 union
	select 206, 'Core', 134 union
	select 207, 'Mezmerize', 135 union
	select 208, '[1997] Black Light Syndrome', 136 union
	select 209, 'Live [Disc 1]', 137 union
	select 210, 'Live [Disc 2]', 137 union
	select 211, 'The Singles', 138 union
	select 212, 'Beyond Good And Evil', 139 union
	select 213, 'Pure Cult: The Best Of The Cult (For Rockers, Ravers, Lovers & Sinners) [UK]', 139 union
	select 214, 'The Doors', 140 union
	select 215, 'The Police Greatest Hits', 141 union
	select 216, 'Hot Rocks, 1964-1971 (Disc 1)', 142 union
	select 217, 'No Security', 142 union
	select 218, 'Voodoo Lounge', 142 union
	select 219, 'Tangents', 143 union
	select 220, 'Transmission', 143 union
	select 221, 'My Generation - The Very Best Of The Who', 144 union
	select 222, 'Serie Sem Limite (Disc 1)', 145 union
	select 223, 'Serie Sem Limite (Disc 2)', 145 union
	select 224, 'Acustico', 146 union
	select 225, 'Volume Dois', 146 union
	select 226, 'Battlestar Galactica: The Story So Far', 147 union
	select 227, 'Battlestar Galactica, Season 3', 147 union
	select 228, 'Heroes, Season 1', 148 union
	select 229, 'Lost, Season 3', 149 union
	select 230, 'Lost, Season 1', 149 union
	select 231, 'Lost, Season 2', 149 union
	select 232, 'Achtung Baby', 150 union
	select 233, 'All That You Can''t Leave Behind', 150 union
	select 234, 'B-Sides 1980-1990', 150 union
	select 235, 'How To Dismantle An Atomic Bomb', 150 union
	select 236, 'Pop', 150 union
	select 237, 'Rattle And Hum', 150 union
	select 238, 'The Best Of 1980-1990', 150 union
	select 239, 'War', 150 union
	select 240, 'Zooropa', 150 union
	select 241, 'UB40 The Best Of - Volume Two [UK]', 151 union
	select 242, 'Diver Down', 152 union
	select 243, 'The Best Of Van Halen, Vol. I', 152 union
	select 244, 'Van Halen', 152 union
	select 245, 'Van Halen III', 152 union
	select 246, 'Contraband', 153 union
	select 247, 'Vinicius De Moraes', 72 union
	select 248, 'Ao Vivo [IMPORT]', 155 union
	select 249, 'The Office, Season 1', 156 union
	select 250, 'The Office, Season 2', 156 union
	select 251, 'The Office, Season 3', 156 union
	select 252, 'Un-Led-Ed', 157 union
	select 253, 'Battlestar Galactica (Classic), Season 1', 158 union
	select 254, 'Aquaman', 159 union
	select 255, 'Instant Karma: The Amnesty International Campaign to Save Darfur', 150 union
	select 256, 'Speak of the Devil', 114 union
	select 257, '20th Century Masters - The Millennium Collection: The Best of Scorpions', 179 union
	select 258, 'House of Pain', 180 union
	select 259, 'Radio Brasil (O Som da Jovem Vanguarda) - Seleccao de Henrique Amaro', 36 union
	select 260, 'Cake: B-Sides and Rarities', 196 union
	select 261, 'LOST, Season 4', 149 union
	select 262, 'Quiet Songs', 197 union
	select 263, 'Muso Ko', 198 union
	select 264, 'Realize', 199 union
	select 265, 'Every Kind of Light', 200 union
	select 266, 'Duos II', 201 union
	select 267, 'Worlds', 202 union
	select 268, 'The Best of Beethoven', 203 union
	select 269, 'Temple of the Dog', 204 union
	select 270, 'Carry On', 205 union
	select 271, 'Revelations', 8 union
	select 272, 'Adorate Deum: Gregorian Chant from the Proper of the Mass', 206 union
	select 273, 'Allegri: Miserere', 207 union
	select 274, 'Pachelbel: Canon & Gigue', 208 union
	select 275, 'Vivaldi: The Four Seasons', 209 union
	select 276, 'Bach: Violin Concertos', 210 union
	select 277, 'Bach: Goldberg Variations', 211 union
	select 278, 'Bach: The Cello Suites', 212 union
	select 279, 'Handel: The Messiah (Highlights)', 213 union
	select 280, 'The World of Classical Favourites', 214 union
	select 281, 'Sir Neville Marriner: A Celebration', 215 union
	select 282, 'Mozart: Wind Concertos', 216 union
	select 283, 'Haydn: Symphonies 99 - 104', 217 union
	select 284, 'Beethoven: Symhonies Nos. 5 & 6', 218 union
	select 285, 'A Soprano Inspired', 219 union
	select 286, 'Great Opera Choruses', 220 union
	select 287, 'Wagner: Favourite Overtures', 221 union
	select 288, 'Faure: Requiem, Ravel: Pavane & Others', 222 union
	select 289, 'Tchaikovsky: The Nutcracker', 223 union
	select 290, 'The Last Night of the Proms', 224 union
	select 291, 'Puccini: Madama Butterfly - Highlights', 225 union
	select 292, 'Holst: The Planets, Op. 32 & Vaughan Williams: Fantasies', 226 union
	select 293, 'Pavarotti''s Opera Made Easy', 227 union
	select 294, 'Great Performances - Barber''s Adagio and Other Romantic Favorites for Strings', 228 union
	select 295, 'Carmina Burana', 229 union
	select 296, 'A Copland Celebration, Vol. I', 230 union
	select 297, 'Bach: Toccata & Fugue in D Minor', 231 union
	select 298, 'Prokofiev: Symphony No.1', 232 union
	select 299, 'Scheherazade', 233 union
	select 300, 'Bach: The Brandenburg Concertos', 234 union
	select 301, 'Chopin: Piano Concertos Nos. 1 & 2', 235 union
	select 302, 'Mascagni: Cavalleria Rusticana', 236 union
	select 303, 'Sibelius: Finlandia', 237 union
	select 304, 'Beethoven Piano Sonatas: Moonlight & Pastorale', 238 union
	select 305, 'Great Recordings of the Century - Mahler: Das Lied von der Erde', 240 union
	select 306, 'Elgar: Cello Concerto & Vaughan Williams: Fantasias', 241 union
	select 307, 'Adams, John: The Chairman Dances', 242 union
	select 308, 'Tchaikovsky: 1812 Festival Overture, Op.49, Capriccio Italien & Beethoven: Wellington''s Victory', 243 union
	select 309, 'Palestrina: Missa Papae Marcelli & Allegri: Miserere', 244 union
	select 310, 'Prokofiev: Romeo & Juliet', 245 union
	select 311, 'Strauss: Waltzes', 226 union
	select 312, 'Berlioz: Symphonie Fantastique', 245 union
	select 313, 'Bizet: Carmen Highlights', 246 union
	select 314, 'English Renaissance', 247 union
	select 315, 'Handel: Music for the Royal Fireworks (Original Version 1749)', 208 union
	select 316, 'Grieg: Peer Gynt Suites & Sibelius: Pelleas et Melisande', 248 union
	select 317, 'Mozart Gala: Famous Arias', 249 union
	select 318, 'SCRIABIN: Vers la flamme', 250 union
	select 319, 'Armada: Music from the Courts of England and Spain', 251 union
	select 320, 'Mozart: Symphonies Nos. 40 & 41', 248 union
	select 321, 'Back to Black', 252 union
	select 322, 'Frank', 252 union
	select 323, 'Carried to Dust (Bonus Track Version)', 253 union
	select 324, 'Beethoven: Symphony No. 6 ''Pastoral'' Etc.', 254 union
	select 325, 'Bartok: Violin & Viola Concertos', 255 union
	select 326, 'Mendelssohn: A Midsummer Night''s Dream', 256 union
	select 327, 'Bach: Orchestral Suites Nos. 1 - 4', 257 union
	select 328, 'Charpentier: Divertissements, Airs & Concerts', 258 union
	select 329, 'South American Getaway', 259 union
	select 330, 'Gorecki: Symphony No. 3', 260 union
	select 331, 'Purcell: The Fairy Queen', 261 union
	select 332, 'The Ultimate Relexation Album', 262 union
	select 333, 'Purcell: Music for the Queen Mary', 263 union
	select 334, 'Weill: The Seven Deadly Sins', 264 union
	select 335, 'J.S. Bach: Chaconne, Suite in E Minor, Partita in E Major & Prelude, Fugue and Allegro', 265 union
	select 336, 'Prokofiev: Symphony No.5 & Stravinksy: Le Sacre Du Printemps', 248 union
	select 337, 'Szymanowski: Piano Works, Vol. 1', 266 union
	select 338, 'Nielsen: The Six Symphonies', 267 union
	select 339, 'Great Recordings of the Century: Paganini''s 24 Caprices', 268 union
	select 340, 'Liszt - 12 Etudes D''Execution Transcendante', 269 union
	select 341, 'Great Recordings of the Century - Shubert: Schwanengesang, 4 Lieder', 270 union
	select 342, 'Locatelli: Concertos for Violin, Strings and Continuo, Vol. 3', 271 union
	select 343, 'Respighi:Pines of Rome', 226 union
	select 344, 'Schubert: The Late String Quartets & String Quintet (3 CD''s)', 272 union
	select 345, 'Monteverdi: L''Orfeo', 273 union
	select 346, 'Mozart: Chamber Music', 274 union
	select 347, 'Koyaanisqatsi (Soundtrack from the Motion Picture)', 275;

	create table tracks as
	  select 1 as trackId, 'For Those About To Rock (We Salute You)' as name, 1 as albumId, 1 as mediaTypeId, 1 as genreId, 'Angus Young, Malcolm Young, Brian Johnson' as composer, 343719 as milliseconds, 11170334 as bytes, 0.99 as unitPrice union
	  select 3, 'Fast As a Shark', 3, 2, 1, 'F. Baltes, S. Kaufman, U. Dirkscneider & W. Hoffman', 230619, 3990994, 0.99 union
	  select 4, 'Restless and Wild', 3, 2, 1, 'F. Baltes, R.A. Smith-Diesel, S. Kaufman, U. Dirkscneider & W. Hoffman', 252051, 4331779, 0.99 union
	  select 5, 'Princess of the Dawn', 3, 2, 1, 'Deaffy & R.A. Smith-Diesel', 375418, 6290521, 0.99 union
	  select 6, 'Put The Finger On You', 1, 1, 1, 'Angus Young, Malcolm Young, Brian Johnson', 205662, 6713451, 0.99 union
	  select 7, 'Let''s Get It Up', 1, 1, 1, 'Angus Young, Malcolm Young, Brian Johnson', 233926, 7636561, 0.99 union
	  select 8, 'Inject The Venom', 1, 1, 1, 'Angus Young, Malcolm Young, Brian Johnson', 210834, 6852860, 0.99 union
	  select 9, 'Snowballed', 1, 1, 1, 'Angus Young, Malcolm Young, Brian Johnson', 203102, 6599424, 0.99 union
	  select 10, 'Evil Walks', 1, 1, 1, 'Angus Young, Malcolm Young, Brian Johnson', 263497, 8611245, 0.99 union
	  select 11, 'C.O.D.', 1, 1, 1, 'Angus Young, Malcolm Young, Brian Johnson', 199836, 6566314, 0.99 union
	  select 12, 'Breaking The Rules', 1, 1, 1, 'Angus Young, Malcolm Young, Brian Johnson', 263288, 8596840, 0.99 union
	  select 13, 'Night Of The Long Knives', 1, 1, 1, 'Angus Young, Malcolm Young, Brian Johnson', 205688, 6706347, 0.99 union
	  select 14, 'Spellbound', 1, 1, 1, 'Angus Young, Malcolm Young, Brian Johnson', 270863, 8817038, 0.99 union
	  select 15, 'Go Down', 4, 1, 1, 'AC/DC', 331180, 10847611, 0.99 union
	  select 16, 'Dog Eat Dog', 4, 1, 1, 'AC/DC', 215196, 7032162, 0.99 union
	  select 17, 'Let There Be Rock', 4, 1, 1, 'AC/DC', 366654, 12021261, 0.99 union
	  select 18, 'Bad Boy Boogie', 4, 1, 1, 'AC/DC', 267728, 8776140, 0.99 union
	  select 19, 'Problem Child', 4, 1, 1, 'AC/DC', 325041, 10617116, 0.99 union
	  select 20, 'Overdose', 4, 1, 1, 'AC/DC', 369319, 12066294, 0.99 union
	  select 21, 'Hell Ain''t A Bad Place To Be', 4, 1, 1, 'AC/DC', 254380, 8331286, 0.99 union
	  select 22, 'Whole Lotta Rosie', 4, 1, 1, 'AC/DC', 323761, 10547154, 0.99 union
	  select 23, 'Walk On Water', 5, 1, 1, 'Steven Tyler, Joe Perry, Jack Blades, Tommy Shaw', 295680, 9719579, 0.99 union
	  select 24, 'Love In An Elevator', 5, 1, 1, 'Steven Tyler, Joe Perry', 321828, 10552051, 0.99 union
	  select 25, 'Rag Doll', 5, 1, 1, 'Steven Tyler, Joe Perry, Jim Vallance, Holly Knight', 264698, 8675345, 0.99 union
	  select 26, 'What It Takes', 5, 1, 1, 'Steven Tyler, Joe Perry, Desmond Child', 310622, 10144730, 0.99 union
	  select 27, 'Dude (Looks Like A Lady)', 5, 1, 1, 'Steven Tyler, Joe Perry, Desmond Child', 264855, 8679940, 0.99 union
	  select 28, 'Janie''s Got A Gun', 5, 1, 1, 'Steven Tyler, Tom Hamilton', 330736, 10869391, 0.99 union
	  select 29, 'Cryin''', 5, 1, 1, 'Steven Tyler, Joe Perry, Taylor Rhodes', 309263, 10056995, 0.99 union
	  select 30, 'Amazing', 5, 1, 1, 'Steven Tyler, Richie Supa', 356519, 11616195, 0.99 union
	  select 31, 'Blind Man', 5, 1, 1, 'Steven Tyler, Joe Perry, Taylor Rhodes', 240718, 7877453, 0.99 union
	  select 32, 'Deuces Are Wild', 5, 1, 1, 'Steven Tyler, Jim Vallance', 215875, 7074167, 0.99 union
	  select 33, 'The Other Side', 5, 1, 1, 'Steven Tyler, Jim Vallance', 244375, 7983270, 0.99 union
	  select 34, 'Crazy', 5, 1, 1, 'Steven Tyler, Joe Perry, Desmond Child', 316656, 10402398, 0.99 union
	  select 35, 'Eat The Rich', 5, 1, 1, 'Steven Tyler, Joe Perry, Jim Vallance', 251036, 8262039, 0.99 union
	  select 36, 'Angel', 5, 1, 1, 'Steven Tyler, Desmond Child', 307617, 9989331, 0.99 union
	  select 37, 'Livin'' On The Edge', 5, 1, 1, 'Steven Tyler, Joe Perry, Mark Hudson', 381231, 12374569, 0.99 union
	  select 38, 'All I Really Want', 6, 1, 1, 'Alanis Morissette & Glenn Ballard', 284891, 9375567, 0.99 union
	  select 39, 'You Oughta Know', 6, 1, 1, 'Alanis Morissette & Glenn Ballard', 249234, 8196916, 0.99 union
	  select 40, 'Perfect', 6, 1, 1, 'Alanis Morissette & Glenn Ballard', 188133, 6145404, 0.99 union
	  select 41, 'Hand In My Pocket', 6, 1, 1, 'Alanis Morissette & Glenn Ballard', 221570, 7224246, 0.99 union
	  select 42, 'Right Through You', 6, 1, 1, 'Alanis Morissette & Glenn Ballard', 176117, 5793082, 0.99 union
	  select 43, 'Forgiven', 6, 1, 1, 'Alanis Morissette & Glenn Ballard', 300355, 9753256, 0.99 union
	  select 44, 'You Learn', 6, 1, 1, 'Alanis Morissette & Glenn Ballard', 239699, 7824837, 0.99 union
	  select 45, 'Head Over Feet', 6, 1, 1, 'Alanis Morissette & Glenn Ballard', 267493, 8758008, 0.99 union
	  select 46, 'Mary Jane', 6, 1, 1, 'Alanis Morissette & Glenn Ballard', 280607, 9163588, 0.99 union
	  select 47, 'Ironic', 6, 1, 1, 'Alanis Morissette & Glenn Ballard', 229825, 7598866, 0.99 union
	  select 48, 'Not The Doctor', 6, 1, 1, 'Alanis Morissette & Glenn Ballard', 227631, 7604601, 0.99 union
	  select 49, 'Wake Up', 6, 1, 1, 'Alanis Morissette & Glenn Ballard', 293485, 9703359, 0.99 union
	  select 50, 'You Oughta Know (Alternate)', 6, 1, 1, 'Alanis Morissette & Glenn Ballard', 491885, 16008629, 0.99 union
	  select 51, 'We Die Young', 7, 1, 1, 'Jerry Cantrell', 152084, 4925362, 0.99 union
	  select 52, 'Man In The Box', 7, 1, 1, 'Jerry Cantrell, Layne Staley', 286641, 9310272, 0.99 union
	  select 53, 'Sea Of Sorrow', 7, 1, 1, 'Jerry Cantrell', 349831, 11316328, 0.99 union
	  select 54, 'Bleed The Freak', 7, 1, 1, 'Jerry Cantrell', 241946, 7847716, 0.99 union
	  select 55, 'I Can''t Remember', 7, 1, 1, 'Jerry Cantrell, Layne Staley', 222955, 7302550, 0.99 union
	  select 56, 'Love, Hate, Love', 7, 1, 1, 'Jerry Cantrell, Layne Staley', 387134, 12575396, 0.99 union
	  select 57, 'It Ain''t Like That', 7, 1, 1, 'Jerry Cantrell, Michael Starr, Sean Kinney', 277577, 8993793, 0.99 union
	  select 58, 'Sunshine', 7, 1, 1, 'Jerry Cantrell', 284969, 9216057, 0.99 union
	  select 59, 'Put You Down', 7, 1, 1, 'Jerry Cantrell', 196231, 6420530, 0.99 union
	  select 60, 'Confusion', 7, 1, 1, 'Jerry Cantrell, Michael Starr, Layne Staley', 344163, 11183647, 0.99 union
	  select 61, 'I Know Somethin (Bout You)', 7, 1, 1, 'Jerry Cantrell', 261955, 8497788, 0.99 union
	  select 62, 'Real Thing', 7, 1, 1, 'Jerry Cantrell, Layne Staley', 243879, 7937731, 0.99 union
	  select 77, 'Enter Sandman', 9, 1, 3, 'Apocalyptica', 221701, 7286305, 0.99 union
	  select 78, 'Master Of Puppets', 9, 1, 3, 'Apocalyptica', 436453, 14375310, 0.99 union
	  select 79, 'Harvester Of Sorrow', 9, 1, 3, 'Apocalyptica', 374543, 12372536, 0.99 union
	  select 80, 'The Unforgiven', 9, 1, 3, 'Apocalyptica', 322925, 10422447, 0.99 union
	  select 81, 'Sad But True', 9, 1, 3, 'Apocalyptica', 288208, 9405526, 0.99 union
	  select 82, 'Creeping Death', 9, 1, 3, 'Apocalyptica', 308035, 10110980, 0.99 union
	  select 83, 'Wherever I May Roam', 9, 1, 3, 'Apocalyptica', 369345, 12033110, 0.99 union
	  select 84, 'Welcome Home (Sanitarium)', 9, 1, 3, 'Apocalyptica', 350197, 11406431, 0.99 union
	  select 85, 'Cochise', 10, 1, 1, 'Audioslave/Chris Cornell', 222380, 5339931, 0.99 union
	  select 86, 'Show Me How to Live', 10, 1, 1, 'Audioslave/Chris Cornell', 277890, 6672176, 0.99 union
	  select 87, 'Gasoline', 10, 1, 1, 'Audioslave/Chris Cornell', 279457, 6709793, 0.99 union
	  select 88, 'What You Are', 10, 1, 1, 'Audioslave/Chris Cornell', 249391, 5988186, 0.99 union
	  select 89, 'Like a Stone', 10, 1, 1, 'Audioslave/Chris Cornell', 294034, 7059624, 0.99 union
	  select 90, 'Set It Off', 10, 1, 1, 'Audioslave/Chris Cornell', 263262, 6321091, 0.99 union
	  select 91, 'Shadow on the Sun', 10, 1, 1, 'Audioslave/Chris Cornell', 343457, 8245793, 0.99 union
	  select 92, 'I am the Highway', 10, 1, 1, 'Audioslave/Chris Cornell', 334942, 8041411, 0.99 union
	  select 93, 'Exploder', 10, 1, 1, 'Audioslave/Chris Cornell', 206053, 4948095, 0.99 union
	  select 94, 'Hypnotize', 10, 1, 1, 'Audioslave/Chris Cornell', 206628, 4961887, 0.99 union
	  select 95, 'Bring''em Back Alive', 10, 1, 1, 'Audioslave/Chris Cornell', 329534, 7911634, 0.99 union
	  select 96, 'Light My Way', 10, 1, 1, 'Audioslave/Chris Cornell', 303595, 7289084, 0.99 union
	  select 97, 'Getaway Car', 10, 1, 1, 'Audioslave/Chris Cornell', 299598, 7193162, 0.99 union
	  select 98, 'The Last Remaining Light', 10, 1, 1, 'Audioslave/Chris Cornell', 317492, 7622615, 0.99 union
	  select 99, 'Your Time Has Come', 11, 1, 4, 'Cornell, Commerford, Morello, Wilk', 255529, 8273592, 0.99 union
	  select 100, 'Out Of Exile', 11, 1, 4, 'Cornell, Commerford, Morello, Wilk', 291291, 9506571, 0.99 union
	  select 101, 'Be Yourself', 11, 1, 4, 'Cornell, Commerford, Morello, Wilk', 279484, 9106160, 0.99 union
	  select 102, 'Doesn''t Remind Me', 11, 1, 4, 'Cornell, Commerford, Morello, Wilk', 255869, 8357387, 0.99 union
	  select 103, 'Drown Me Slowly', 11, 1, 4, 'Cornell, Commerford, Morello, Wilk', 233691, 7609178, 0.99 union
	  select 104, 'Heaven''s Dead', 11, 1, 4, 'Cornell, Commerford, Morello, Wilk', 276688, 9006158, 0.99 union
	  select 105, 'The Worm', 11, 1, 4, 'Cornell, Commerford, Morello, Wilk', 237714, 7710800, 0.99 union
	  select 106, 'Man Or Animal', 11, 1, 4, 'Cornell, Commerford, Morello, Wilk', 233195, 7542942, 0.99 union
	  select 107, 'Yesterday To Tomorrow', 11, 1, 4, 'Cornell, Commerford, Morello, Wilk', 273763, 8944205, 0.99 union
	  select 108, 'Dandelion', 11, 1, 4, 'Cornell, Commerford, Morello, Wilk', 278125, 9003592, 0.99 union
	  select 109, '#1 Zero', 11, 1, 4, 'Cornell, Commerford, Morello, Wilk', 299102, 9731988, 0.99 union
	  select 110, 'The Curse', 11, 1, 4, 'Cornell, Commerford, Morello, Wilk', 309786, 10029406, 0.99 union
	  select 111, 'Money', 12, 1, 5, 'Berry Gordy, Jr./Janie Bradford', 147591, 2365897, 0.99 union
	  select 112, 'Long Tall Sally', 12, 1, 5, 'Enotris Johnson/Little Richard/Robert "Bumps" Blackwell', 106396, 1707084, 0.99 union
	  select 113, 'Bad Boy', 12, 1, 5, 'Larry Williams', 116088, 1862126, 0.99 union
	  select 114, 'Twist And Shout', 12, 1, 5, 'Bert Russell/Phil Medley', 161123, 2582553, 0.99 union
	  select 115, 'Please Mr. Postman', 12, 1, 5, 'Brian Holland/Freddie Gorman/Georgia Dobbins/Robert Bateman/William Garrett', 137639, 2206986, 0.99 union
	  select 116, 'C''Mon Everybody', 12, 1, 5, 'Eddie Cochran/Jerry Capehart', 140199, 2247846, 0.99 union
	  select 117, 'Rock ''N'' Roll Music', 12, 1, 5, 'Chuck Berry', 141923, 2276788, 0.99 union
	  select 118, 'Slow Down', 12, 1, 5, 'Larry Williams', 163265, 2616981, 0.99 union
	  select 119, 'Roadrunner', 12, 1, 5, 'Bo Diddley', 143595, 2301989, 0.99 union
	  select 120, 'Carol', 12, 1, 5, 'Chuck Berry', 143830, 2306019, 0.99 union
	  select 121, 'Good Golly Miss Molly', 12, 1, 5, 'Little Richard', 106266, 1704918, 0.99 union
	  select 122, '20 Flight Rock', 12, 1, 5, 'Ned Fairchild', 107807, 1299960, 0.99 union
	  select 123, 'Quadrant', 13, 1, 2, 'Billy Cobham', 261851, 8538199, 0.99 union
	  select 124, 'Snoopy''s search-Red baron', 13, 1, 2, 'Billy Cobham', 456071, 15075616, 0.99 union
	  select 125, 'Spanish moss-"A sound portrait"-Spanish moss', 13, 1, 2, 'Billy Cobham', 248084, 8217867, 0.99 union
	  select 126, 'Moon germs', 13, 1, 2, 'Billy Cobham', 294060, 9714812, 0.99 union
	  select 127, 'Stratus', 13, 1, 2, 'Billy Cobham', 582086, 19115680, 0.99 union
	  select 128, 'The pleasant pheasant', 13, 1, 2, 'Billy Cobham', 318066, 10630578, 0.99 union
	  select 129, 'Solo-Panhandler', 13, 1, 2, 'Billy Cobham', 246151, 8230661, 0.99 union
	  select 130, 'Do what cha wanna', 13, 1, 2, 'George Duke', 274155, 9018565, 0.99 union
	  select 156, 'Wheels Of Confusion / The Straightener', 17, 1, 3, 'Tony Iommi, Bill Ward, Geezer Butler, Ozzy Osbourne', 494524, 16065830, 0.99 union
	  select 157, 'Tomorrow''s Dream', 17, 1, 3, 'Tony Iommi, Bill Ward, Geezer Butler, Ozzy Osbourne', 192496, 6252071, 0.99 union
	  select 158, 'Changes', 17, 1, 3, 'Tony Iommi, Bill Ward, Geezer Butler, Ozzy Osbourne', 286275, 9175517, 0.99 union
	  select 159, 'FX', 17, 1, 3, 'Tony Iommi, Bill Ward, Geezer Butler, Ozzy Osbourne', 103157, 3331776, 0.99 union
	  select 160, 'Supernaut', 17, 1, 3, 'Tony Iommi, Bill Ward, Geezer Butler, Ozzy Osbourne', 285779, 9245971, 0.99 union
	  select 161, 'Snowblind', 17, 1, 3, 'Tony Iommi, Bill Ward, Geezer Butler, Ozzy Osbourne', 331676, 10813386, 0.99 union
	  select 162, 'Cornucopia', 17, 1, 3, 'Tony Iommi, Bill Ward, Geezer Butler, Ozzy Osbourne', 234814, 7653880, 0.99 union
	  select 163, 'Laguna Sunrise', 17, 1, 3, 'Tony Iommi, Bill Ward, Geezer Butler, Ozzy Osbourne', 173087, 5671374, 0.99 union
	  select 164, 'St. Vitus Dance', 17, 1, 3, 'Tony Iommi, Bill Ward, Geezer Butler, Ozzy Osbourne', 149655, 4884969, 0.99 union
	  select 165, 'Under The Sun/Every Day Comes and Goes', 17, 1, 3, 'Tony Iommi, Bill Ward, Geezer Butler, Ozzy Osbourne', 350458, 11360486, 0.99 union
	  select 183, 'King In Crimson', 19, 1, 3, 'Roy Z', 283167, 9218499, 0.99 union
	  select 184, 'Chemical Wedding', 19, 1, 3, 'Roy Z', 246177, 8022764, 0.99 union
	  select 185, 'The Tower', 19, 1, 3, 'Roy Z', 285257, 9435693, 0.99 union
	  select 186, 'Killing Floor', 19, 1, 3, 'Adrian Smith', 269557, 8854240, 0.99 union
	  select 187, 'Book Of Thel', 19, 1, 3, 'Eddie Casillas/Roy Z', 494393, 16034404, 0.99 union
	  select 188, 'Gates Of Urizen', 19, 1, 3, 'Roy Z', 265351, 8627004, 0.99 union
	  select 189, 'Jerusalem', 19, 1, 3, 'Roy Z', 402390, 13194463, 0.99 union
	  select 190, 'Trupets Of Jericho', 19, 1, 3, 'Roy Z', 359131, 11820908, 0.99 union
	  select 191, 'Machine Men', 19, 1, 3, 'Adrian Smith', 341655, 11138147, 0.99 union
	  select 192, 'The Alchemist', 19, 1, 3, 'Roy Z', 509413, 16545657, 0.99 union
	  select 193, 'Realword', 19, 1, 3, 'Roy Z', 237531, 7802095, 0.99 union
	  select 194, 'First Time I Met The Blues', 20, 1, 6, 'Eurreal Montgomery', 140434, 4604995, 0.99 union
	  select 195, 'Let Me Love You Baby', 20, 1, 6, 'Willie Dixon', 175386, 5716994, 0.99 union
	  select 196, 'Stone Crazy', 20, 1, 6, 'Buddy Guy', 433397, 14184984, 0.99 union
	  select 197, 'Pretty Baby', 20, 1, 6, 'Willie Dixon', 237662, 7848282, 0.99 union
	  select 198, 'When My Left Eye Jumps', 20, 1, 6, 'Al Perkins/Willie Dixon', 235311, 7685363, 0.99 union
	  select 199, 'Leave My Girl Alone', 20, 1, 6, 'Buddy Guy', 204721, 6859518, 0.99 union
	  select 200, 'She Suits Me To A Tee', 20, 1, 6, 'Buddy Guy', 136803, 4456321, 0.99 union
	  select 201, 'Keep It To Myself (Aka Keep It To Yourself)', 20, 1, 6, 'Sonny Boy Williamson [I]', 166060, 5487056, 0.99 union
	  select 202, 'My Time After Awhile', 20, 1, 6, 'Robert Geddins/Ron Badger/Sheldon Feinberg', 182491, 6022698, 0.99 union
	  select 203, 'Too Many Ways (Alternate)', 20, 1, 6, 'Willie Dixon', 135053, 4459946, 0.99 union
	  select 204, 'Talkin'' ''Bout Women Obviously', 20, 1, 6, 'Amos Blakemore/Buddy Guy', 589531, 19161377, 0.99 union
	  select 205, 'Jorge Da Capadocia', 21, 1, 7, 'Jorge Ben', 177397, 5842196, 0.99 union
	  select 206, 'Prenda Minha', 21, 1, 7, 'Tradicional', 99369, 3225364, 0.99 union
	  select 207, 'Meditacao', 21, 1, 7, 'Tom Jobim - Newton Mendoca', 148793, 4865597, 0.99 union
	  select 208, 'Terra', 21, 1, 7, 'Caetano Veloso', 482429, 15889054, 0.99 union
	  select 209, 'Eclipse Oculto', 21, 1, 7, 'Caetano Veloso', 221936, 7382703, 0.99 union
	  select 210, 'Texto "Verdade Tropical"', 21, 1, 7, 'Caetano Veloso', 84088, 2752161, 0.99 union
	  select 211, 'Bem Devagar', 21, 1, 7, 'Gilberto Gil', 133172, 4333651, 0.99 union
	  select 212, 'Drao', 21, 1, 7, 'Gilberto Gil', 156264, 5065932, 0.99 union
	  select 213, 'Saudosismo', 21, 1, 7, 'Caetano Veloso', 144326, 4726981, 0.99 union
	  select 214, 'Carolina', 21, 1, 7, 'Chico Buarque', 181812, 5924159, 0.99 union
	  select 215, 'Sozinho', 21, 1, 7, 'Peninha', 190589, 6253200, 0.99 union
	  select 216, 'Esse Cara', 21, 1, 7, 'Caetano Veloso', 223111, 7217126, 0.99 union
	  select 217, 'Mel', 21, 1, 7, 'Caetano Veloso - Waly Salomao', 294765, 9854062, 0.99 union
	  select 218, 'Linha Do Equador', 21, 1, 7, 'Caetano Veloso - Djavan', 299337, 10003747, 0.99 union
	  select 219, 'Odara', 21, 1, 7, 'Caetano Veloso', 141270, 4704104, 0.99 union
	  select 220, 'A Luz De Tieta', 21, 1, 7, 'Caetano Veloso', 251742, 8507446, 0.99 union
	  select 221, 'Atras Da Verd-E-Rosa So Nao Vai Quem Ja Morreu', 21, 1, 7, 'David Correa - Paulinho Carvalho - Carlos Sena - Bira do Ponto', 307252, 10364247, 0.99 union
	  select 222, 'Vida Boa', 21, 1, 7, 'Fausto Nilo - Armandinho', 281730, 9411272, 0.99 union
	  select 246, 'Mateus Enter', 24, 1, 7, 'Chico Science', 33149, 1103013, 0.99 union
	  select 247, 'O Cidadao Do Mundo', 24, 1, 7, 'Chico Science', 200933, 6724966, 0.99 union
	  select 248, 'Etnia', 24, 1, 7, 'Chico Science', 152555, 5061413, 0.99 union
	  select 249, 'Quilombo Groove [Instrumental]', 24, 1, 7, 'Chico Science', 151823, 5042447, 0.99 union
	  select 250, 'Maco', 24, 1, 7, 'Chico Science', 249600, 8253934, 0.99 union
	  select 251, 'Um Passeio No Mundo Livre', 24, 1, 7, 'Chico Science', 240091, 7984291, 0.99 union
	  select 252, 'Samba Do Lado', 24, 1, 7, 'Chico Science', 227317, 7541688, 0.99 union
	  select 253, 'Maracatu Atomico', 24, 1, 7, 'Chico Science', 284264, 9670057, 0.99 union
	  select 254, 'O Encontro De Isaac Asimov Com Santos Dumont No Ceu', 24, 1, 7, 'Chico Science', 99108, 3240816, 0.99 union
	  select 255, 'Corpo De Lama', 24, 1, 7, 'Chico Science', 232672, 7714954, 0.99 union
	  select 256, 'Sobremesa', 24, 1, 7, 'Chico Science', 240091, 7960868, 0.99 union
	  select 257, 'Manguetown', 24, 1, 7, 'Chico Science', 194560, 6475159, 0.99 union
	  select 258, 'Um Satelite Na Cabeca', 24, 1, 7, 'Chico Science', 126615, 4272821, 0.99 union
	  select 259, 'Baiao Ambiental [Instrumental]', 24, 1, 7, 'Chico Science', 152659, 5198539, 0.99 union
	  select 260, 'Sangue De Bairro', 24, 1, 7, 'Chico Science', 132231, 4415557, 0.99 union
	  select 261, 'Enquanto O Mundo Explode', 24, 1, 7, 'Chico Science', 88764, 2968650, 0.99 union
	  select 262, 'Interlude Zumbi', 24, 1, 7, 'Chico Science', 71627, 2408550, 0.99 union
	  select 263, 'Crianca De Domingo', 24, 1, 7, 'Chico Science', 208222, 6984813, 0.99 union
	  select 264, 'Amor De Muito', 24, 1, 7, 'Chico Science', 175333, 5881293, 0.99 union
	  select 265, 'Samidarish [Instrumental]', 24, 1, 7, 'Chico Science', 272431, 8911641, 0.99 union
	  select 266, 'Maracatu Atomico [Atomic Version]', 24, 1, 7, 'Chico Science', 273084, 9019677, 0.99 union
	  select 267, 'Maracatu Atomico [Ragga Mix]', 24, 1, 7, 'Chico Science', 210155, 6986421, 0.99 union
	  select 268, 'Maracatu Atomico [Trip Hop]', 24, 1, 7, 'Chico Science', 221492, 7380787, 0.99 union
	  select 282, 'Girassol', 26, 1, 8, 'Bino Farias/Da Gama/Lazao/Pedro Luis/Toni Garrido', 249808, 8327676, 0.99 union
	  select 283, 'A Sombra Da Maldade', 26, 1, 8, 'Da Gama/Toni Garrido', 230922, 7697230, 0.99 union
	  select 284, 'Johnny B. Goode', 26, 1, 8, 'Chuck Berry', 254615, 8505985, 0.99 union
	  select 285, 'Soldado Da Paz', 26, 1, 8, 'Herbert Vianna', 194220, 6455080, 0.99 union
	  select 286, 'Firmamento', 26, 1, 8, 'Bino Farias/Da Gama/Henry Lawes/Lazao/Toni Garrido/Winston Foser-Vers', 222145, 7402658, 0.99 union
	  select 287, 'Extra', 26, 1, 8, 'Gilberto Gil', 304352, 10078050, 0.99 union
	  select 288, 'O Ere', 26, 1, 8, 'Bernardo Vilhena/Bino Farias/Da Gama/Lazao/Toni Garrido', 236382, 7866924, 0.99 union
	  select 289, 'Podes Crer', 26, 1, 8, 'Bino Farias/Da Gama/Lazao/Toni Garrido', 232280, 7747747, 0.99 union
	  select 290, 'A Estrada', 26, 1, 8, 'Bino Farias/Da Gama/Lazao/Toni Garrido', 248842, 8275673, 0.99 union
	  select 291, 'Berlim', 26, 1, 8, 'Da Gama/Toni Garrido', 207542, 6920424, 0.99 union
	  select 292, 'Ja Foi', 26, 1, 8, 'Bino Farias/Da Gama/Lazao/Toni Garrido', 221544, 7388466, 0.99 union
	  select 293, 'Onde Voce Mora?', 26, 1, 8, 'Marisa Monte/Nando Reis', 256026, 8502588, 0.99 union
	  select 294, 'Pensamento', 26, 1, 8, 'Bino Farias/Da Gamma/Lazao/Ras Bernard', 173008, 5748424, 0.99 union
	  select 295, 'Conciliacao', 26, 1, 8, 'Da Gama/Lazao/Ras Bernardo', 257619, 8552474, 0.99 union
	  select 296, 'Realidade Virtual', 26, 1, 8, 'Bino Farias/Da Gama/Lazao/Toni Garrido', 195239, 6503533, 0.99 union
	  select 297, 'Mensagem', 26, 1, 8, 'Bino Farias/Da Gama/Lazao/Ras Bernardo', 225332, 7488852, 0.99 union
	  select 298, 'A Cor Do Sol', 26, 1, 8, 'Bernardo Vilhena/Da Gama/Lazao', 231392, 7663348, 0.99 union
	  select 299, 'Onde Voce Mora?', 27, 1, 8, 'Marisa Monte/Nando Reis', 298396, 10056970, 0.99 union
	  select 300, 'O Ere', 27, 1, 8, 'Bernardo Vilhena/Bino/Da Gama/Lazao/Toni Garrido', 206942, 6950332, 0.99 union
	  select 301, 'A Sombra Da Maldade', 27, 1, 8, 'Da Gama/Toni Garrido', 285231, 9544383, 0.99 union
	  select 302, 'A Estrada', 27, 1, 8, 'Da Gama/Lazao/Toni Garrido', 282174, 9344477, 0.99 union
	  select 303, 'Falar A Verdade', 27, 1, 8, 'Bino/Da Gama/Ras Bernardo', 244950, 8189093, 0.99 union
	  select 304, 'Firmamento', 27, 1, 8, 'Harry Lawes/Winston Foster-Vers', 225488, 7507866, 0.99 union
	  select 305, 'Pensamento', 27, 1, 8, 'Bino/Da Gama/Ras Bernardo', 192391, 6399761, 0.99 union
	  select 306, 'Realidade Virtual', 27, 1, 8, 'Bino/Da Gamma/Lazao/Toni Garrido', 240300, 8069934, 0.99 union
	  select 307, 'Doutor', 27, 1, 8, 'Bino/Da Gama/Toni Garrido', 178155, 5950952, 0.99 union
	  select 308, 'Na Frente Da TV', 27, 1, 8, 'Bino/Da Gama/Lazao/Ras Bernardo', 289750, 9633659, 0.99 union
	  select 309, 'Downtown', 27, 1, 8, 'Cidade Negra', 239725, 8024386, 0.99 union
	  select 310, 'Sabado A Noite', 27, 1, 8, 'Lulu Santos', 267363, 8895073, 0.99 union
	  select 311, 'A Cor Do Sol', 27, 1, 8, 'Bernardo Vilhena/Da Gama/Lazao', 273031, 9142937, 0.99 union
	  select 312, 'Eu Tambem Quero Beijar', 27, 1, 8, 'Fausto Nilo/Moraes Moreira/Pepeu Gomes', 211147, 7029400, 0.99 union
	  select 323, 'Dig-Dig, Lambe-Lambe (Ao Vivo)', 29, 1, 9, 'Cassiano Costa/Cintia Maviane/J.F./Lucas Costa', 205479, 6892516, 0.99 union
	  select 324, 'Perere', 29, 1, 9, 'Augusto Conceicao/Chiclete Com Banana', 198661, 6643207, 0.99 union
	  select 325, 'TriboTchan', 29, 1, 9, 'Cal Adan/Paulo Levi', 194194, 6507950, 0.99 union
	  select 326, 'Tapa Aqui, Descobre Ali', 29, 1, 9, 'Paulo Levi/W. Rangel', 188630, 6327391, 0.99 union
	  select 327, 'Daniela', 29, 1, 9, 'Jorge Cardoso/Pierre Onasis', 230791, 7748006, 0.99 union
	  select 328, 'Bate Lata', 29, 1, 9, 'Fabio Nolasco/Gal Sales/Ivan Brasil', 206733, 7034985, 0.99 union
	  select 329, 'Garotas do Brasil', 29, 1, 9, 'Garay, Ricardo Engels/Luca Predabom/Ludwig, Carlos Henrique/Mauricio Vieira', 210155, 6973625, 0.99 union
	  select 330, 'Levada do Amor (Ailoviu)', 29, 1, 9, 'Luiz Wanderley/Paulo Levi', 190093, 6457752, 0.99 union
	  select 331, 'Lavadeira', 29, 1, 9, 'Do Vale, Valverde/Gal Oliveira/Luciano Pinto', 214256, 7254147, 0.99 union
	  select 332, 'Reboladeira', 29, 1, 9, 'Cal Adan/Ferrugem/Julinho Carioca/Triona Ni Dhomhnaill', 210599, 7027525, 0.99 union
	  select 333, 'E que Nessa Encarnacao Eu Nasci Manga', 29, 1, 9, 'Lucina/Luli', 196519, 6568081, 0.99 union
	  select 334, 'Reggae Tchan', 29, 1, 9, 'Cal Adan/Del Rey, Tension/Edu Casanova', 206654, 6931328, 0.99 union
	  select 335, 'My Love', 29, 1, 9, 'Jauperi/Zeu Goes', 203493, 6772813, 0.99 union
	  select 336, 'Latinha de Cerveja', 29, 1, 9, 'Adriano Bernandes/Edmar Neves', 166687, 5532564, 0.99 union
	  select 337, 'You Shook Me', 30, 1, 1, 'J B Lenoir/Willie Dixon', 315951, 10249958, 0.99 union
	  select 338, 'I Can''t Quit You Baby', 30, 1, 1, 'Willie Dixon', 263836, 8581414, 0.99 union
	  select 339, 'Communication Breakdown', 30, 1, 1, 'Jimmy Page/John Bonham/John Paul Jones', 192653, 6287257, 0.99 union
	  select 340, 'Dazed and Confused', 30, 1, 1, 'Jimmy Page', 401920, 13035765, 0.99 union
	  select 341, 'The Girl I Love She Got Long Black Wavy Hair', 30, 1, 1, 'Jimmy Page/John Bonham/John Estes/John Paul Jones/Robert Plant', 183327, 5995686, 0.99 union
	  select 342, 'What is and Should Never Be', 30, 1, 1, 'Jimmy Page/Robert Plant', 260675, 8497116, 0.99 union
	  select 343, 'Communication Breakdown(2)', 30, 1, 1, 'Jimmy Page/John Bonham/John Paul Jones', 161149, 5261022, 0.99 union
	  select 344, 'Travelling Riverside Blues', 30, 1, 1, 'Jimmy Page/Robert Johnson/Robert Plant', 312032, 10232581, 0.99 union
	  select 345, 'Whole Lotta Love', 30, 1, 1, 'Jimmy Page/John Bonham/John Paul Jones/Robert Plant/Willie Dixon', 373394, 12258175, 0.99 union
	  select 346, 'Somethin'' Else', 30, 1, 1, 'Bob Cochran/Sharon Sheeley', 127869, 4165650, 0.99 union
	  select 347, 'Communication Breakdown(3)', 30, 1, 1, 'Jimmy Page/John Bonham/John Paul Jones', 185260, 6041133, 0.99 union
	  select 348, 'I Can''t Quit You Baby(2)', 30, 1, 1, 'Willie Dixon', 380551, 12377615, 0.99 union
	  select 349, 'You Shook Me(2)', 30, 1, 1, 'J B Lenoir/Willie Dixon', 619467, 20138673, 0.99 union
	  select 350, 'How Many More Times', 30, 1, 1, 'Chester Burnett/Jimmy Page/John Bonham/John Paul Jones/Robert Plant', 711836, 23092953, 0.99 union
	  select 351, 'Debra Kadabra', 31, 1, 1, 'Frank Zappa', 234553, 7649679, 0.99 union
	  select 352, 'Carolina Hard-Core Ecstasy', 31, 1, 1, 'Frank Zappa', 359680, 11731061, 0.99 union
	  select 353, 'Sam With The Showing Scalp Flat Top', 31, 1, 1, 'Don Van Vliet', 171284, 5572993, 0.99 union
	  select 354, 'Poofter''s Froth Wyoming Plans Ahead', 31, 1, 1, 'Frank Zappa', 183902, 6007019, 0.99 union
	  select 355, '200 Years Old', 31, 1, 1, 'Frank Zappa', 272561, 8912465, 0.99 union
	  select 356, 'Cucamonga', 31, 1, 1, 'Frank Zappa', 144483, 4728586, 0.99 union
	  select 357, 'Advance Romance', 31, 1, 1, 'Frank Zappa', 677694, 22080051, 0.99 union
	  select 358, 'Man With The Woman Head', 31, 1, 1, 'Don Van Vliet', 88894, 2922044, 0.99 union
	  select 359, 'Muffin Man', 31, 1, 1, 'Frank Zappa', 332878, 10891682, 0.99 union
	  select 374, 'Guanabara', 33, 1, 7, 'Marcos Valle', 247614, 8499591, 0.99 union
	  select 375, 'Mas Que Nada', 33, 1, 7, 'Jorge Ben', 248398, 8255254, 0.99 union
	  select 376, 'Voo Sobre o Horizonte', 33, 1, 7, 'J.r.Bertami/Parana', 225097, 7528825, 0.99 union
	  select 377, 'A Paz', 33, 1, 7, 'Donato/Gilberto Gil', 263183, 8619173, 0.99 union
	  select 378, 'Wave (Vou te Contar)', 33, 1, 7, 'Antonio Carlos Jobim', 271647, 9057557, 0.99 union
	  select 379, 'Agua de Beber', 33, 1, 7, 'Antonio Carlos Jobim/Vinicius de Moraes', 146677, 4866476, 0.99 union
	  select 380, 'Samba da Bencaco', 33, 1, 7, 'Baden Powell/Vinicius de Moraes', 282200, 9440676, 0.99 union
	  select 381, 'Pode Parar', 33, 1, 7, 'Jorge Vercilo/Jota Maranhao', 179408, 6046678, 0.99 union
	  select 382, 'Menino do Rio', 33, 1, 7, 'Caetano Veloso', 262713, 8737489, 0.99 union
	  select 383, 'Ando Meio Desligado', 33, 1, 7, 'Caetano Veloso', 195813, 6547648, 0.99 union
	  select 384, 'Misterio da Raca', 33, 1, 7, 'Luiz Melodia/Ricardo Augusto', 184320, 6191752, 0.99 union
	  select 385, 'All Star', 33, 1, 7, 'Nando Reis', 176326, 5891697, 0.99 union
	  select 386, 'Menina Bonita', 33, 1, 7, 'Alexandre Brazil/Pedro Luis/Rodrigo Cabelo', 237087, 7938246, 0.99 union
	  select 387, 'Pescador de Ilusoes', 33, 1, 7, 'Macelo Yuka/O Rappa', 245524, 8267067, 0.99 union
	  select 388, 'A Vontade (Live Mix)', 33, 1, 7, 'Bombom/Ed Motta', 180636, 5972430, 0.99 union
	  select 389, 'Maria Fumaca', 33, 1, 7, 'Luiz Carlos/Oberdan', 141008, 4743149, 0.99 union
	  select 390, 'Sambassim (dj patife remix)', 33, 1, 7, 'Alba Carvalho/Fernando Porto', 213655, 7243166, 0.99 union
	  select 391, 'Garota De Ipanema', 34, 1, 7, 'Varios', 279536, 9141343, 0.99 union
	  select 392, 'Tim Tim Por Tim Tim', 34, 1, 7, 'Varios', 213237, 7143328, 0.99 union
	  select 393, 'Tarde Em Itapoa', 34, 1, 7, 'Varios', 313704, 10344491, 0.99 union
	  select 394, 'Tanto Tempo', 34, 1, 7, 'Varios', 170292, 5572240, 0.99 union
	  select 395, 'Eu Vim Da Bahia - Live', 34, 1, 7, 'Varios', 157988, 5115428, 0.99 union
	  select 396, 'Alo Alo Marciano', 34, 1, 7, 'Varios', 238106, 8013065, 0.99 union
	  select 397, 'Linha Do Horizonte', 34, 1, 7, 'Varios', 279484, 9275929, 0.99 union
	  select 398, 'Only A Dream In Rio', 34, 1, 7, 'Varios', 371356, 12192989, 0.99 union
	  select 399, 'Abrir A Porta', 34, 1, 7, 'Varios', 271960, 8991141, 0.99 union
	  select 400, 'Alice', 34, 1, 7, 'Varios', 165982, 5594341, 0.99 union
	  select 401, 'Momentos Que Marcam', 34, 1, 7, 'Varios', 280137, 9313740, 0.99 union
	  select 402, 'Um Jantar Pra Dois', 34, 1, 7, 'Varios', 237714, 7819755, 0.99 union
	  select 403, 'Bumbo Da Mangueira', 34, 1, 7, 'Varios', 270158, 9073350, 0.99 union
	  select 404, 'Mr Funk Samba', 34, 1, 7, 'Varios', 213890, 7102545, 0.99 union
	  select 405, 'Santo Antonio', 34, 1, 7, 'Varios', 162716, 5492069, 0.99 union
	  select 406, 'Por Voce', 34, 1, 7, 'Varios', 205557, 6792493, 0.99 union
	  select 407, 'So Tinha De Ser Com Voce', 34, 1, 7, 'Varios', 389642, 13085596, 0.99 union
	  select 408, 'Free Speech For The Dumb', 35, 1, 3, 'Molaney/Morris/Roberts/Wainwright', 155428, 5076048, 0.99 union
	  select 409, 'It''s Electric', 35, 1, 3, 'Harris/Tatler', 213995, 6978601, 0.99 union
	  select 410, 'Sabbra Cadabra', 35, 1, 3, 'Black Sabbath', 380342, 12418147, 0.99 union
	  select 411, 'Turn The Page', 35, 1, 3, 'Seger', 366524, 11946327, 0.99 union
	  select 412, 'Die Die My Darling', 35, 1, 3, 'Danzig', 149315, 4867667, 0.99 union
	  select 413, 'Loverman', 35, 1, 3, 'Cave', 472764, 15446975, 0.99 union
	  select 414, 'Mercyful Fate', 35, 1, 3, 'Diamond/Shermann', 671712, 21942829, 0.99 union
	  select 415, 'Astronomy', 35, 1, 3, 'A.Bouchard/J.Bouchard/S.Pearlman', 397531, 13065612, 0.99 union
	  select 416, 'Whiskey In The Jar', 35, 1, 3, 'Traditional', 305005, 9943129, 0.99 union
	  select 417, 'Tuesday''s Gone', 35, 1, 3, 'Collins/Van Zandt', 545750, 17900787, 0.99 union
	  select 418, 'The More I See', 35, 1, 3, 'Molaney/Morris/Roberts/Wainwright', 287973, 9378873, 0.99 union
	  select 419, 'A Kind Of Magic', 36, 1, 1, 'Roger Taylor', 262608, 8689618, 0.99 union
	  select 420, 'Under Pressure', 36, 1, 1, 'Queen & David Bowie', 236617, 7739042, 0.99 union
	  select 421, 'Radio GA GA', 36, 1, 1, 'Roger Taylor', 343745, 11358573, 0.99 union
	  select 422, 'I Want It All', 36, 1, 1, 'Queen', 241684, 7876564, 0.99 union
	  select 423, 'I Want To Break Free', 36, 1, 1, 'John Deacon', 259108, 8552861, 0.99 union
	  select 424, 'Innuendo', 36, 1, 1, 'Queen', 387761, 12664591, 0.99 union
	  select 425, 'It''s A Hard Life', 36, 1, 1, 'Freddie Mercury', 249417, 8112242, 0.99 union
	  select 426, 'Breakthru', 36, 1, 1, 'Queen', 249234, 8150479, 0.99 union
	  select 427, 'Who Wants To Live Forever', 36, 1, 1, 'Brian May', 297691, 9577577, 0.99 union
	  select 428, 'Headlong', 36, 1, 1, 'Queen', 273057, 8921404, 0.99 union
	  select 429, 'The Miracle', 36, 1, 1, 'Queen', 294974, 9671923, 0.99 union
	  select 430, 'I''m Going Slightly Mad', 36, 1, 1, 'Queen', 248032, 8192339, 0.99 union
	  select 431, 'The Invisible Man', 36, 1, 1, 'Queen', 238994, 7920353, 0.99 union
	  select 432, 'Hammer To Fall', 36, 1, 1, 'Brian May', 220316, 7255404, 0.99 union
	  select 433, 'Friends Will Be Friends', 36, 1, 1, 'Freddie Mercury & John Deacon', 248920, 8114582, 0.99 union
	  select 434, 'The Show Must Go On', 36, 1, 1, 'Queen', 263784, 8526760, 0.99 union
	  select 435, 'One Vision', 36, 1, 1, 'Queen', 242599, 7936928, 0.99 union
	  select 436, 'Detroit Rock City', 37, 1, 1, 'Paul Stanley, B. Ezrin', 218880, 7146372, 0.99 union
	  select 437, 'Black Diamond', 37, 1, 1, 'Paul Stanley', 314148, 10266007, 0.99 union
	  select 438, 'Hard Luck Woman', 37, 1, 1, 'Paul Stanley', 216032, 7109267, 0.99 union
	  select 439, 'Sure Know Something', 37, 1, 1, 'Paul Stanley, Vincent Poncia', 242468, 7939886, 0.99 union
	  select 440, 'Love Gun', 37, 1, 1, 'Paul Stanley', 196257, 6424915, 0.99 union
	  select 441, 'Deuce', 37, 1, 1, 'Gene Simmons', 185077, 6097210, 0.99 union
	  select 442, 'Goin'' Blind', 37, 1, 1, 'Gene Simmons, S. Coronel', 216215, 7045314, 0.99 union
	  select 443, 'Shock Me', 37, 1, 1, 'Ace Frehley', 227291, 7529336, 0.99 union
	  select 444, 'Do You Love Me', 37, 1, 1, 'Paul Stanley, B. Ezrin, K. Fowley', 214987, 6976194, 0.99 union
	  select 445, 'She', 37, 1, 1, 'Gene Simmons, S. Coronel', 248346, 8229734, 0.99 union
	  select 446, 'I Was Made For Loving You', 37, 1, 1, 'Paul Stanley, Vincent Poncia, Desmond Child', 271360, 9018078, 0.99 union
	  select 447, 'Shout It Out Loud', 37, 1, 1, 'Paul Stanley, Gene Simmons, B. Ezrin', 219742, 7194424, 0.99 union
	  select 448, 'God Of Thunder', 37, 1, 1, 'Paul Stanley', 255791, 8309077, 0.99 union
	  select 449, 'Calling Dr. Love', 37, 1, 1, 'Gene Simmons', 225332, 7395034, 0.99 union
	  select 450, 'Beth', 37, 1, 1, 'S. Penridge, Bob Ezrin, Peter Criss', 166974, 5360574, 0.99 union
	  select 451, 'Strutter', 37, 1, 1, 'Paul Stanley, Gene Simmons', 192496, 6317021, 0.99 union
	  select 452, 'Rock And Roll All Nite', 37, 1, 1, 'Paul Stanley, Gene Simmons', 173609, 5735902, 0.99 union
	  select 453, 'Cold Gin', 37, 1, 1, 'Ace Frehley', 262243, 8609783, 0.99 union
	  select 454, 'Plaster Caster', 37, 1, 1, 'Gene Simmons', 207333, 6801116, 0.99 union
	  select 455, 'God Gave Rock ''n'' Roll To You', 37, 1, 1, 'Paul Stanley, Gene Simmons, Rus Ballard, Bob Ezrin', 320444, 10441590, 0.99 union
	  select 468, 'Maria', 39, 1, 4, 'Billie Joe Armstrong -Words Green Day -Music', 167262, 5484747, 0.99 union
	  select 469, 'Poprocks And Coke', 39, 1, 4, 'Billie Joe Armstrong -Words Green Day -Music', 158354, 5243078, 0.99 union
	  select 470, 'Longview', 39, 1, 4, 'Billie Joe Armstrong -Words Green Day -Music', 234083, 7714939, 0.99 union
	  select 471, 'Welcome To Paradise', 39, 1, 4, 'Billie Joe Armstrong -Words Green Day -Music', 224208, 7406008, 0.99 union
	  select 472, 'Basket Case', 39, 1, 4, 'Billie Joe Armstrong -Words Green Day -Music', 181629, 5951736, 0.99 union
	  select 473, 'When I Come Around', 39, 1, 4, 'Billie Joe Armstrong -Words Green Day -Music', 178364, 5839426, 0.99 union
	  select 474, 'She', 39, 1, 4, 'Billie Joe Armstrong -Words Green Day -Music', 134164, 4425128, 0.99 union
	  select 475, 'J.A.R. (Jason Andrew Relva)', 39, 1, 4, 'Mike Dirnt -Words Green Day -Music', 170997, 5645755, 0.99 union
	  select 476, 'Geek Stink Breath', 39, 1, 4, 'Billie Joe Armstrong -Words Green Day -Music', 135888, 4408983, 0.99 union
	  select 477, 'Brain Stew', 39, 1, 4, 'Billie Joe Armstrong -Words Green Day -Music', 193149, 6305550, 0.99 union
	  select 478, 'Jaded', 39, 1, 4, 'Billie Joe Armstrong -Words Green Day -Music', 90331, 2950224, 0.99 union
	  select 479, 'Walking Contradiction', 39, 1, 4, 'Billie Joe Armstrong -Words Green Day -Music', 151170, 4932366, 0.99 union
	  select 480, 'Stuck With Me', 39, 1, 4, 'Billie Joe Armstrong -Words Green Day -Music', 135523, 4431357, 0.99 union
	  select 481, 'Hitchin'' A Ride', 39, 1, 4, 'Billie Joe Armstrong -Words Green Day -Music', 171546, 5616891, 0.99 union
	  select 482, 'Good Riddance (Time Of Your Life)', 39, 1, 4, 'Billie Joe Armstrong -Words Green Day -Music', 153600, 5075241, 0.99 union
	  select 483, 'Redundant', 39, 1, 4, 'Billie Joe Armstrong -Words Green Day -Music', 198164, 6481753, 0.99 union
	  select 484, 'Nice Guys Finish Last', 39, 1, 4, 'Billie Joe Armstrong -Words Green Day -Music', 170187, 5604618, 0.99 union
	  select 485, 'Minority', 39, 1, 4, 'Billie Joe Armstrong -Words Green Day -Music', 168803, 5535061, 0.99 union
	  select 486, 'Warning', 39, 1, 4, 'Billie Joe Armstrong -Words Green Day -Music', 221910, 7343176, 0.99 union
	  select 487, 'Waiting', 39, 1, 4, 'Billie Joe Armstrong -Words Green Day -Music', 192757, 6316430, 0.99 union
	  select 488, 'Macy''s Day Parade', 39, 1, 4, 'Billie Joe Armstrong -Words Green Day -Music', 213420, 7075573, 0.99 union
	  select 489, 'Into The Light', 40, 1, 1, 'David Coverdale', 76303, 2452653, 0.99 union
	  select 490, 'River Song', 40, 1, 1, 'David Coverdale', 439510, 14359478, 0.99 union
	  select 491, 'She Give Me ...', 40, 1, 1, 'David Coverdale', 252551, 8385478, 0.99 union
	  select 492, 'Don''t You Cry', 40, 1, 1, 'David Coverdale', 347036, 11269612, 0.99 union
	  select 493, 'Love Is Blind', 40, 1, 1, 'David Coverdale/Earl Slick', 344999, 11409720, 0.99 union
	  select 494, 'Slave', 40, 1, 1, 'David Coverdale/Earl Slick', 291892, 9425200, 0.99 union
	  select 495, 'Cry For Love', 40, 1, 1, 'Bossi/David Coverdale/Earl Slick', 293015, 9567075, 0.99 union
	  select 496, 'Living On Love', 40, 1, 1, 'Bossi/David Coverdale/Earl Slick', 391549, 12785876, 0.99 union
	  select 497, 'Midnight Blue', 40, 1, 1, 'David Coverdale/Earl Slick', 298631, 9750990, 0.99 union
	  select 498, 'Too Many Tears', 40, 1, 1, 'Adrian Vanderberg/David Coverdale', 359497, 11810238, 0.99 union
	  select 499, 'Don''t Lie To Me', 40, 1, 1, 'David Coverdale/Earl Slick', 283585, 9288007, 0.99 union
	  select 500, 'Wherever You May Go', 40, 1, 1, 'David Coverdale', 239699, 7803074, 0.99;


-- Question 2
CREATE TABLE pricing as
  select "REPLACE THIS LINE WITH YOUR SOLUTION";


-- Question 3
CREATE TABLE long as
  select "REPLACE THIS LINE WITH YOUR SOLUTION";


-- Question 4
CREATE TABLE largest as
  select "REPLACE THIS LINE WITH YOUR SOLUTION";


-- Question 5
CREATE TABLE long_album as
  select "REPLACE THIS LINE WITH YOUR SOLUTION";


-- Question 6
CREATE TABLE track_count as
  select "REPLACE THIS LINE WITH YOUR SOLUTION";


-- Question 7
CREATE TABLE album_count as
  select "REPLACE THIS LINE WITH YOUR SOLUTION";


-- Question 8
CREATE TABLE busiest_artists as
  select "REPLACE THIS LINE WITH YOUR SOLUTION";


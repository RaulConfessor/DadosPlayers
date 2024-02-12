CREATE DATABASE FIFA
GO

USE FIFA
GO

CREATE TABLE PLAYERS(
	ID_PLAYERS INT PRIMARY KEY,
	SHORT_NAME VARCHAR(40) NOT NULL,
	LONG_NAME VARCHAR (90) NOT NULL,
	AGE INT NOT NULL,
	OVERALL INT NOT NULL,
	POTENTIAL INT NOT NULL,
	HEIGHT_CM INT NOT NULL,
	WEIGHT_KG INT NOT NULL,
	NATIONALITY VARCHAR(20) NOT NULL,
	CLUB VARCHAR (50) NOT NULL,
	VALUE_EUR INT NOT NULL,
	WAGE_EUR INT NOT NULL,
	POSITIONS VARCHAR(20) NOT NULL,
	PREFERRED_FOOT VARCHAR(5) NOT NULL, 
	INTERNAT_REPUTION INT NOT NULL
)
GO

SELECT * FROM PLAYERS
GO

SELECT * FROM PLAYERS
WHERE POTENTIAL >=91 and AGE <=25
GO

/*
Tabela de Jogadores:

ID_PLAYERS    SHORT_NAME              LONG_NAME                     AGE    OVERALL    POTENTIAL    HEIGHT_CM    WEIGHT_KG    NATIONALITY    CLUB                      VALUE_EUR    WAGE_EUR    POSITIONS    PREFERRED_FOOT    INTERNAT_REPUTION
202126        H. Kane                 Harry Kane                    25     89         91           188          89           England        Tottenham Hotspur       83000000     220000      ST           Right            3
210257        Ederson                 Ederson Santana de Moraes     25     88         91           188          86           Brazil         Manchester City          54500000     185000      GK           Left             2
211110        P. Dybala               Paulo Bruno Exequiel Dybala   25     88         92           177          75           Argentina      Juventus                 76500000     215000      CAM, RW      Left             3
222492        L. Sané                 Leroy Sané                    23     86         92           183          75           Germany        Manchester City          61000000     195000      LW           Left             2
228702        F. de Jong              Frenkie de Jong               22     85         91           180          74           Netherlands    FC Barcelona             52000000     195000      CM, CDM      Right            3
230621        G. Donnarumma           Gianluigi Donnarumma          20     85         92           196          90           Italy          Milan                    41500000     34000       GK           Right            3
231747        K. Mbappé               Kylian Mbappé                 20     89         95           178          73           France         Paris Saint-Germain      93500000     155000      ST, RW       Right            3
233049        J. Sancho               Jadon Sancho                  19     84         92           180          76           England        Borussia Dortmund        44500000     61000       RM, LM       Right            2
235243        M. de Ligt              Matthijs de Ligt              19     85         93           189          89           Netherlands    Juventus                 50000000     76000       CB           Right            3
235790        K. Havertz              Kai Havertz                   20     84         92           188          83           Germany        Bayer 04 Leverkusen      46000000     70000       CAM, RM      Left             1
238794        Vinícius Jr.            Vinícius José de Oliveira Júnior 18  79         92           176          73           Brazil         Real Madrid              22500000     60000       LW           Right            2
242444        João Félix              João Félix Sequeira           19     80         93           181          70           Portugal       Atlético Madrid          28000000     38000       CF, ST       Right            1
*/

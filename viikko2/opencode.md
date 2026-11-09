# OpenCode-kokemukset (GPT-6 Luna)

## top_goal_scorers

Agentti toteutti metodin docstringin mukaisesti, mutta tyyli poikkesi luokan muusta koodista. Agentti käytti
`[:how_many]` ja yhden rivin ratkaisua, kun taas luokan toinen metodi rakentaa listan
silmukassa. Lambda-muuttujan nimi oli `player`, muualla `p`. Ratkaisu on kuitenkin
selkeä ja toimiva.

Agentti tarkisti koodin komennolla `python3 -m compileall`, joka käytti koneen
Python 3.12:ta eikä projektin 3.14:ää, eikä tarkistus kertonut mitään koodin
toimivuudesta tai Pylint-säännöistä.

## Pylint-varoituksen selitys

Agentin oma muutos `index.py`:hin aiheutti varoituksen `R0915: Too many statements (16/10)`. Agenitn selitys varoitukselle
piti paikkansa: "sääntö laskee lauseita eikä rivejä, ja sen tarkoitus
on pitää funktiot luettavina ja helposti ylläpidettävinä". Selityksestä puuttui kuitenkin maininta siitä että 10 raja tulee projektin
`.pylintrc`:stä, kun taas Pylintin oletusraja on 50.

## Toimiko ratkaisu, ja testit?

Joukkuehaku näytti toimivan agentin omissa tarkistuksissa, mutta oikealla datalla
löytyi virhe. Vertailu `player.team == team` ei löytänyt kesken kauden siirtyneitä
pelaajia, koska heidän `team`-kentässään on useita joukkueita. Agentin testidatassa
jokaisella pelaajalla oli vain yksi joukkue, joten se ei huomannut virhettä. Korjasin
virheen lisäämällä `Player`-luokkaan `teams`-ominaisuuden.

Agentti muutti myös koodia enemmän kuin pyysin. Se lisäsi käyttöliittymään hakutavan
valinnan ja `Quit`-vaihtoehdon ja muutti taulukon otsikkoa.

Testit agentti teki pyynnöstäni stubilla, mutta testien ajaminen ei aluksi toiminut, koska pytestiä ei ollut asennettu. Agentti
asensi sen kuitenkin lopulta oikein komennolla `uv add --dev pytest` eikä pipillä.

## Ero edellisen viikon testeihin

Perusmalli oli sama: stub, jolla on `get_players`-metodi, ja oikeat
`Player`-oliot. Erona lähinnä se että reunatapauksia (esim. tyhjä tulos) ei testattu ilman erillistä pyyntöä

## Löysikö Pylint virheitä?

Agentin muutokset kasvattivat `main`-funktion 16 lauseeseen, vaikka raja oli 10.
Korjasin sen siirtämällä hakulogiikan omaan `ask_players`-funktioon. Korjausten
jälkeen agentin koodi, myös testit, läpäisivät testit.

## Mitä muuta opin

- Agentille syötetyissä kehotteissa on syytä olla tarkat vaatimukset.
- Agentti tekee helposti enemmän kuin pyydetään, joten `git diff` kannattaa lukea
  kokonaan ennen committia.
- Agentin selitykset ovat hyödyllisiä, mutta ne kannattaa tarkistaa. Agentti kutsui esimerkiksi `team`-kenttää maajoukkueeksi.

Bálint Dániel HL6ENQ
2. Data Product

Másodjára szeretnék olyat alkotni, ami nagyban eltér az előzőtől, és valamilyen szinten új információkat nyújt, nem pedig már sokszor látottat. Az alap koncepció, hogy a számítógép képernyőjét pásztázom folyamatosan egy programmal és a pixelek színéről tárolok el adatokat. Ezt azért a folyamatos képernyőképekből nyerem ki, mivel így nem csak egyes programokat tudok elemezni, hanem tényleg azt, amit a felhasználó csinál és lát. 

Annak érdekében, hogy a már az újonnan szerzett adatkezeléses tudásomat is be tudjam vetni, ezt python-ban szeretném megvalósítani. Terveim szerint screenshot-ot készítek a képernyőről, és ennek a képnek elemzem ki minden pixelét RGB színösszetétel alapján. Már utána olvastam pár library-nek, amik rendkívül gyorsan képesek képeket elemezni, és screenshot-ot készíteni, szóval bizakodó vagyok, hogy ez a művelet sorozat egy végtelen ciklusban a valós eredményeket adja majd vissza a látottakról. Az adatok tárolására egy SQLite adatbázist tervezek használni, ugyanis ez gyorsabb mintha fájlba írnék, plusz szebb megoldás.

Amiért ez az ötlet megszületett az az volt, hogy egy ismerősömnek meséltem egy filmről, amit láttam, és ez neki megtetszett, de ő nem nézhette meg mivel már volt ilyentől epilepsziás rohama. Amennyiben én legközelebb filmet nézek, elindíthatom ezt a programot és a későbbiekben ki tudom nyerni az adatokból, hogy mennyire is villódzanak a képek, jelent-e bárimilyen kockázatot az erre érzékeny embereknek. 

Keresgélésem során rábukkantam egy ötletre, miszerint ezeket a színeket valós időben felhasználhatom arra is, hogy egy LED szalagra küldöm őket, így kiterjesztve egy egész szobára a képernyő hangulatát. (Ehhez meg is rendeltem egy arduinot, de tekintettel a szállítási időre, ezt nem biztos, hogy meg tudom valósítani.)

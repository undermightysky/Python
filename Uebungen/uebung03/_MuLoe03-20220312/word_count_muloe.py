# -*- coding: utf-8 -*-

text = '''Man findet wohl kaum jemanden im 21. Jahrhundert, der nicht wüsste,
was eine Datei ist. Auch wenn nicht jeder eine exakte Definition geben könnte,
also beispielsweise: Eine Datei ist eine Menge von logisch zusammenhängenden
und meist sequentiell geordneten Daten, die auf einem Speichermedium dauerhaft
gespeichert werden und mittels eines Bezeichners bzw. Namens wieder
identifizierbar und damit ansprechbar sind. Die Daten einer Datei existieren
also über die Laufzeit eines Programms hinaus. Deswegen werden sie auch als
nicht-flüchtig oder persistent bezeichnet. Auch wenn es so scheinen mag: Das
Wort Datei ist kein altes deutsches Wort. Es ist eine künstliche Schöpfung des
Deutschen Instituts für Normung (DIN). Die beiden Wörter Daten und Kartei
wurden zu dem neuen Wort Datei verschmolzen. Ein solches Kunstwort wird
übrigens als Portmanteau oder Kofferwort bezeichnet. Der Inhalt jeder Datei
besteht grundsätzlich aus einer eindimensionalen Aneinanderreihung von Bits,
die normalerweise in Byte-Blöcken zusammengefasst interpretiert werden. Die
Bytes erhalten erst durch Anwendungsprogramme und das Betriebssystem eine
Bedeutung. Sie entscheiden also, ob es sich um eine Textdatei, ein ausführbares
Programm oder beispielsweise ein Musikstück oder ein Bild handelt.
'''

num_words = len(text.split())
print(f"The text contains {num_words} "
      f"{'word' if num_words==1 else 'words'}.")

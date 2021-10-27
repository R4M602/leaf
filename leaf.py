from funktionen import *


anfangen = input("Bist du bereit in ein neues Abenteuer zu ziehen? (j/n)").lower().strip()               #mit .lower() sage ich, dass alles klein geschrieben wird und mit .strip() sage ich, dass es keine Leerzeichen enthalten soll.

münze = 200
leben = 3



if anfangen == "j":
    print("\ncool das du mitmachst und wünsche dir eine coole reise")
    name = input("\nalso dann benenne doch mal deinen Charakter! ").lower() 
    print(name + " so dann lass uns loslegen")


    geschichte()

    prüfen = input("Bist du bereit diesen Menschen retten zu gehen?(j/n)").lower()                   #Ich will damit prüfen ob der Spieler auch wirklich bereit diesen Menschen retten zu gehen.

    
    if prüfen == "j":
        answer()

        decision = input("\nSo jetzt musst du dich entscheiden, willst du rechts(r), oder links(l)").lower()

        
        if decision == "r":
            print("\nDu probierst mit aller Mühe die Krokodile auszuweichen, doch ohne Erfolg")
            leben = 3 - 1                                                                                   #Jetzt, dass er eine Falsche Antwort gesagt hat, verliert er ein Leben.
            print("\nEs tut mir leid doch du hast nur noch 2 Leben!")
            rechts()
            waffenshop = input("\nAlso bist interessiert an ihm?(j/n)")
            if waffenshop == "j" and leben > 0:
                waffe = input("\nWas willst du für eine Waffe. Ein Maschinengewehr für 40 Münzen oder eine Pistole für 20 Münzen? (Maschinengewehr=j Pistole=n)").lower()           #HIer lasse ich den Spieler eine Waffe auswählen!
                if waffe == "j" and münze >= 40:
                    waffe1()
                    münze = münze - 40
                    print("\nDu hast nur noch " + str(münze) + " Münzen")

                    Waffe()
                    zelt = input("Willst du ein gutes Zelt bauen für 80 Münzen oder willst du ein schlechteres Zelt für 30 Münzen kaufen? gutes= j / schlechtes = n ")

                    if zelt == "j":
                        print("Dies ist eine superentscheidung, denn so kannst du gut und ruhig schlafen.")
                        print("Super du hast immer noch " + str(leben) + " leben")
                    else:
                        print("Danke für Ihren Einkauf.")
                        print("Als du schlafen gehst, fiel die Struktur des Zeltes auf dein Gesicht und du erstickst!")
                        leben = leben - 1
                        print("Du hast nur noch " + str(leben) + " leben")

                elif waffe == "n" and münze >= 20:
                    waffe1()
                    münze = münze - 20
                    print("\nDu hast nur noch "+ str(münze) + " Münzen")

                    Waffe()
                    zelt = input("Willst du ein gutes Zelt bauen für 80 Münzen oder willst du ein schlechteres Zelt für 30 Münzen kaufen? gutes= j / schlechtes = n ")

                    if zelt == "j" and münze >= 80:
                        print("Dies ist eine superentscheidung, denn so kannst du gut und ruhig schlafen.")
                        print("Super du hast immer noch " + str(leben) + " leben")
                    elif zelt == "n" and münze >= 30:
                        print("Danke für Ihren Einkauf.")
                        print("Als du schlafen gehst, fiel die Struktur des Zeltes auf dein Gesicht und du erstickst!")
                        leben = leben - 1
                        print("Du hast nur noch " + str(leben) + " leben")
                    else:
                        print("Es tut mir leid, doch du hast nicht genug Münzen")
                        münzenzahlen = input("Willst du für 1 Leben 100 Münzen kaufen? wenn nicht hast du direkt verloren!")
 
                        if münzenzahlen == "j" and leben > 1:
                            münze = münze + 100
                            leben = leben -1
                            print("super du hast wieder " + str(münze) + "Münzen und " + leben + "Leben")
                        
                        
                        if leben <= 1 :
                            print("sorry du hast deine leben gegen die Münzen gewechselt, so hast du keine leben mehr zu weiter spielen.")

                        

            elif  waffenshop == "n" and leben >0:
                keineWaffe()
                wald = input("\nWillst du in dem Wald gehen oder lieber nicht?(j/n)").lower()
                if wald == "j":
                    todimWald()
                    leben = leben - 1
                    print("\nDu hast nur noch 1 Leben")
                else:
                    nichtWald()
                  
            else:
                gameOver()

        if decision == "l":
            print("\nDu wolltest sicher gehen und gehst deshalb den linken Weg entlang. Du hast natürlich die richtige Entscheidung getroffen!")
            print("\nDas ist super! Denn jetzt hast du noch 3 Leben!")
    
            links()
            katze = input("\nWillst du schauen gehen oder verzichtest du drauf und rennst weg?(j = Du gehst schauen  n = weg rennen)").lower()                  #Hier probiere ich den Spieler zu verwirren 
            if katze == "j":
                print("\nDu gehst mit sehr viel vorsicht schauen und bemerkst, dass es nur eine Katze ist!")
                todkatze()
                insteaddeath()
                gameOver()

            
            elif katze == "n":
                print("\nDu rennst mit aller kraft weg und plötzlich fällst du in einer Höhle wo es stockdunkel ist!")
                fakel = input("Willst du für 10 Münzen eine Fackel kaufen oder lieber eine Taschenlampe für 25 Münzen?(f = Fackel/t = Taschenlampe)").lower()           #Hier lasse ich den Spieler entscheiden ob er eine Fackel oder eine Taschenlampe
                if fakel == "f" and münze >= 10:
                    print("\nSuper du sichst jetzt etwas ist zwar nicht so viel, wie mit einer Taschenlampe aber man kann damit leben!")
                    münze = münze - 10
                    print("\nDu hast nur noch " + str(münze) + " Münzen")
                    inhoehle()
                    pfad = input("willst du diesem Pfad entlang gehen? j/n")
                    if pfad == "j":
                        print("Du beginnst diesem Pfad hindurch zu laufen und plötzlich, bemerkst du das dies eine kleine Brücke ist!")
                        print("Jetzt gibt es kein zurück mehr! Plötzlich beginnt die Brücke zusammen zufallen")
                        print("Du bist Leider gestorben und kannst wegen den schweren Verletzungen nicht weiterfahren!")
                        gameOver()
                    
                    else:
                        print("Glücklicherweise, hast du dich dagegen entschieden, denn es war eine Brücke die nach einigen Minuten eingestürzt ist.")

                    
                elif fakel == "t" and münze >= 25:
                    print("\nSuper das ist viel Geld aber es lohnt sich, jetzt siehst du schon mehr als mit einer Fackel")
                    münze = münze - 25
                    print("\nDu hast nur noch " + str(münze) + " Münzen")
                    inhoehle()
                    pfad = input("willst du diesem Pfad entlang gehen?j/n")

                    if pfad == "j":
                        print("Du beginnst diesem Pfad hindurch zu laufen und plötzlich, bemerkst du das dies eine kleine Brücke ist!")
                        print("Jetzt gibt es kein zurück mehr! Plötzlich beginnt die Brücke zusammen zufallen")
                        print("Du bist Leider gestorben und kannst wegen den schweren Verletzungen nicht weiterfahren!")
                        gameOver()
                    
                    else:
                        print("Glücklicherweise, hast du dich dagegen entschieden, denn es war eine Brücke die nach einigen Minuten eingestürzt ist.")


   
    else:
        print("\nSchade, dass du ihn nicht helfen gehst!")
else:
    print("\nDas tut mir sehr leid!")


               
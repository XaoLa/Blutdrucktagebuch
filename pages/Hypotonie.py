import streamlit as st
st.title('Hypertonie und Hypotonie)

st.subheader('Hypertonie')
st.write('**Definition:** Hypertonie liegt vor, wenn der Blutdruck dauerhaft über 140/90 mmHg liegt.') 
multi = ''' **Ursachen**
- **Genetische Veranlagung:** Familiäre Häufung von Bluthochdruck.
- **Lebensstilfaktoren:** Übergewicht, salzreiche Ernährung, Bewegungsmangel, Stress, Alkohol- und Tabakkonsum.
- **Alter:** Risiko steigt mit zunehmendem Alter. 
- **Geschlecht:** Männer sind häufiger betroffen; Frauen nach der Menopause ebenfalls hohes Risiko. 
- **Sekundäre Ursachen:** Nierenerkrankungen, hormonelle Störungen, Schlafapnoe, bestimmte Medikamente, Herz-Kreislauf-Erkrankungen, Schwangerschaftsbedingter Bluthochdruck (Präeklampsie). 
'''
st.markdown(multi)     
 
multi = ''' **Behandlung**
- **Lebensstiländerungen:** Gewichtsreduktion, salzarme Ernährung, regelmäßige körperliche Aktivität, Stressmanagement, Verzicht auf Alkohol und Nikotin.  
- **Medikamente:** Diuretika, Betablocker, ACE-Hemmer, Angiotensin-II-Rezeptorblocker, Kalziumkanalblocker.   
- Behandlung zugrunde liegender Erkrankungen
'''
st.markdown(multi)


st.subheader('Hypotonie')
st.write('**Definition:** Hypotonie liegt vor, wenn der Blutdruck unter 90/60 mmHg liegt.') 
multi = ''' **Ursachen**  
- **Dehydration:** Flüssigkeitsmangel durch unzureichende Aufnahme oder übermäßigen Verlust.
- **Längeres Liegen:** Bettlägerigkeit.
- **Herzerkrankungen:** Herzinsuffizienz, Herzklappenprobleme, langsamer Herzschlag (Bradykardie).  
- **Blutverlust:** Akute oder chronische Blutungen.  
- **Nährstoffmängel:** Mangel an Vitamin B12 und Folsäure.  
- **Medikamente:** Diuretika, Betablocker, Antidepressiva.  
- **Anaphylaxie:** Schwere allergische Reaktionen.
'''
st.markdown(multi)

multi = ''' **Behandlung**  
- Ausreichende Flüssigkeitszufuhr  
- Anpassung der Ernährung  
- Überprüfung und Anpassung von Medikamenten  
- Behandlung zugrunde liegender Erkrankungen  
- Langsame Positionswechsel
'''
st.markdown(multi)

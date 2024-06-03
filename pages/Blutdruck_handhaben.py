import streamlit as st
st.title('Nicht medikamentöse Maßnahmen')
st.subheader('Erhörter Blutdruck')
st.write('**DASH-Diät:** Ernährungsweise mit viel Obst, Gemüse, Vollkornprodukten, mageren Proteinen und fettarmen Milchprodukten.') 
st.write('**Salzkonsum reduzieren:** Nicht mehr als 5-6 Gramm Salz pro Tag.') 
st.write('**Regelmäßige körperliche Aktivität Ausdauersport:** Mindestens 30 Minuten moderate Bewegung an den meisten Tagen der Woche (z.B. schnelles Gehen, Joggen, Radfahren).') 
st.write('**Gewichtskontrolle Gewichtsreduktion:** Erreichen und Halten eines gesunden BMI und Reduzierung des Bauchumfangs.') 
st.write('**Verzicht auf Rauchen und Alkohol:** Signifikante Verbesserung der allgemeinen Gesundheit und Blutdrucksenkung.') 
st.write('**Salzkonsum verringern:** Ein geringerer Salzkonsum ist vorteilhaft für die Senkung eines erhöhten Blutdrucks')

st.subheader ('Erniegrigter Blutdruck') 
st.write('**Mahlzeiten:** Häufigere kleine Mahlzeiten helfen, den Blutdruck stabil zu halten.') 
st.write('**Langsame Positionswechsel:** Vermeidung plötzlicher Wechsel von einer liegenden oder sitzenden in eine stehende Position, um Schwindel und Blutdruckabfall zu vermeiden.')
st.write('**Kompressionsstrümpfe:** Diese können helfen, das Blut zurück zum Herzen zu pumpen und den Blutdruck zu erhöhen.')
st.write('**Ausreichende Flüssigkeitszufuhr:** Mindestens  2-3 Liter Flüssigkeit pro Tag, vorzugsweise Wasser oder ungesüßter Tee.')
st.write('**Salzkonsum erhöhren:** In Absprache mit dem Arzt kann eine moderate Erhöhung des Salzkonsums helfen, den Blutdruck zu erhöhen.')



multi = '''**Mahlzeiten:** Häufigere kleine Mahlzeiten helfen, den Blutdruck stabil zu halten.  
**Langsame Positionswechsel:** Vermeidung plötzlic

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

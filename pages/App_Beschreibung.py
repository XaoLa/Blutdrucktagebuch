import streamlit as st
st.title('App Beschreibung')
st.write('Herzlich Willkommen bei der Blutdrucktagebuch App, Ihrer persönlichen Unterstützung zur Regulierung von Blutdruck. Diese Anleitung hilft Ihnen, die App optimal zu nutzen, um sowohl Hypotonie als auch Hypertonie effektiv zu managen.')
st.write('**Blutdruckmessung eingeben und verfolgen:** Die genaue und regelmäßige Eingabe Ihrer Blutdruckwerte ist entscheidend für die Überwachung und Verbesserung Ihrer Gesundheit. Hier finden Sie eine detaillierte Anleitung, wie Sie Ihre Blutdruckmessungen eingeben, verfolgen und analysieren können.')
st.write('**Schritt-für-Schritt-Anleitung zur Eingabe von Blutdruckmessungen:**') 
st.write('**Login/Register:** Loggen Sie sich mit Ihrem Benutzernamen ein. Falls Sie neu hier sind, erstellen Sie einfach ein neues Konto')
st.write('**Blutdruckwerte hinzufügen:** Wählen Sie das Datum und die Uhrzeit und tragen Sie dann Ihre Blutdruckwerte ein, sie werden automatisch gespeichert. Nutzen Sie die Buttons „Woche“ und „Monat“, um Ihre Blutdruckwerte über verschiedene Zeiträume hinweg grafisch darzustellen. Diese Visualisierungen helfen Ihnen, Veränderungen und Trends in Ihrem Blutdruck besser zu verstehen.')

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

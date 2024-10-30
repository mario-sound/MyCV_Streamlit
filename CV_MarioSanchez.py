from pathlib import Path

import streamlit as st
from PIL import Image

# General Settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
page_icon = "https://img.icons8.com/?size=100&id=3404&format=png&color=000000"
page_title = "Mario Sánchez CV Audio Dev"
profile_pic = current_dir / "assets" / "image.png"
description = "Te ayudo con la producción de audio de tu podcast o videojuego. También te ayudo a mejorar o crear tu podcast desde 0. Y encima, programo cosas."
resume_file = current_dir / "assets" / "Mario_Sanchez_Linkedin_CV.pdf"
email="info@digitalaudiotips.com"
social_media = {
    "LinkedIn":"https://www.linkedin.com/in/mariosanchezsonido/",
    "YouTube":"https://www.youtube.com/@DigitalAudioTips",
    "GitHub":"https://github.com/mario-sound",
    "DigitalAudioTips":"https://digitalaudiotips.com/",
}
css_file = current_dir / "styles" / "main.css"

# Título y icono de la página
st.set_page_config(page_title=page_title, page_icon=page_icon)


# CSS
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
if resume_file.exists():
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
else:
    st.error("El archivo PDF de CV no se encontró.")
profile_pic = Image.open(profile_pic)

# Primera sección, foto, título, descripción, CV en PDF y mail
col1, col2= st.columns([1.5,3], gap="small")
with col1:
    st.image(profile_pic, width=None)

with col2:
    st.title("Mario Sánchez Molina")
    st.write(description)
    with open(resume_file, "rb") as file:
        st.download_button("Descarga mi CV",
                           data=PDFbyte,
                           file_name="CV_MarioSanchezMolina.pdf")
    st.write("📩", email)
#st.divider()

# Segunda sección, descripción y link
cols = st.columns(len(social_media))
for index, (platform, link) in enumerate(social_media.items()):
    cols[index].write(f"[{platform}]({link})")
st.write('''
Soy un ingeniero de sonido, pero **no** te voy a ofrecer servicios de audio.
- Una empresa que es capaz de ofrecer efectividad y confianza puede acceder a proyectos de cientos de miles de euros. Para ello hay que tener la preparación adecuada.
- Me definen **más de 10 años de experiencia** en el sector del audio, en los que he abordado proyectos de _primera división_.
- Sé **gestionar equipos y coordinar producción** eficientemente. Me encanta enseñar cómo he aprendido a hacerlo. También conozco las herramientas que una empresa
necesita para ofrecer este servicio y yo puedo poner esas herramientas a disposición de mis clientes.
- He trabajado con las mejores empresas del sector de la localización de videojuegos en español, he participado en la producción de **más de 100 videojuegos** y es un trabajo que me encanta.

Compruebalo aquí: https://www.doblajevideojuegos.es/fichatecnico/mario-sanchez-molina
         ''')
#st.write("#") # Esto simplemente es un separador que no estoy usando
#st.divider() # Esto simplemente es un separador
st.markdown("---")  # Crea un separador horizontal

# Tercera sección, Experiencia, estudios, proyectos e idiomas como desplegables.
with st.expander("Experiencia laboral"):
    st.subheader("Production & Management")
    st.write('''
             - Production Assistant - :orange[Lionbridge] _[Septiembre 2023 - Actualidad]_ _:grey[Freelance]_
             - Audio Lead Backup - :orange[Lionbridge] _[Agosto 2024 - Actualidad]_ _:grey[Freelance]_
             - Audio Production Manager - :red[Lil'Box Sound Studio] - _[Septiembre 2022 - Actualidad]_ _:grey[Freelance]_
             - Technical Audio Production - :red[Adio fm] _[Abril 2023 - Abril 2024]_ _:grey[Freelance]_
             - Production Planner - :orange[Storytel] _[Abril 2021 - Julio 2022]_
             
             Diferentes tareas relacionadas con la **producción y coordinación** de audio. Algunas tareas como coordinación de proveedores :grey[(estudios de grabación, locutores y proof listeners)]
             para cumplir con la producción de audiolibros, coordinación de actores de doblaje y técnicos para cumplir con la producción de doblaje de videojuegos. Elaboración de presupuestos,
             gestión del estudio, trato con clientes y proveedores, resolución de conflictos, mediación entre partes, responsabilidad técnica de proyectos entre otras tareas relacionadas con gestión.
             ''')
    st.subheader("Audio Engineering")
    st.write('''
             - Senior Audio Engineer - :orange[Lionbridge] _[Dic 2019 - May 2021] - [Sep 2023 - Sep 2024]_ _:grey[Freelance]_
             - Senior Audio Engineer - :red[Onda Estudios] _[Feb 2020 - Jul 2021] - [Sep 2022 - Oct 2024]_ _:grey[Freelance]_
             - Audio Engineer - :blue[Megara D.A.] _[Marzo 2023 - Junio 2024]_ _:grey[Freelance]_
             - Sound Designer - :orange[Naolito Animation Studios] _[Marzo 2023 - Junio 2023]_ _:grey[Freelance]_
             - Senior Audio Engineer - :orange[Storytel] _[Julio 2020 - Abril 2021]_ _:grey[Freelance]_
             - Senior Audio Engineer - :blue[Keywords Studios] _[Septiembre 2018 - Diciembre 2019]_ _:grey[Freelance]_
             - Audio Engineer - :grey[CrisLama] _[Abril 2018 - Septiembre 2018]_ _:grey[Freelance]_
             - Audio Engineer - :blue[Keywords Studios] _[Marzo 2018 - Abril 2019]_
             - Audio Engineer - :violet[Kite Team] _[Octubre 2015 - Marzo 2018]_
             
             Diferentes tareas relacionadas con la **producción, edición, grabación, mezcla y diseño** de audio. Desde grabación y edición de foley, grabación edición y mezcla de doblaje
             de videojuegos, diseño sonoro para videos corporativos, videos promocionales para videojuegos, podcasts, ficciones sonoras, e-learnings, series de TV. También la grabación
             de artistas musicales, incluyendo producción musical en estudio. Además de ambientación musical para programas de TV.
             ''')
    
    st.subheader("Otros")
    st.write('''
             - Editor audio - :green[CrisCris Producciones] _[Septiembre 2014 - Agosto 2015]_ _:grey[Becario]_
             - Técnico de sistemas - :green[Proyecta Sistemas de Información] _[Abril 2014 - Julio 2014]_ _:grey[Becario]_
             
             Edición de audio, gestión de sistemas informáticos, reparación de equipos, soporte en ofimática y en redes, peparación de equipos de trabajo.
             ''')

with st.expander("Educación y certificados"):
    st.subheader("Programación")
    st.write('''
             - Master Desarrollo Full Stack.Programación Web - :green[Conquer Blocks] _[Enero 2024 - Actualmente]_
             _:grey[HTML5, CSS, JavaScript, Streamlit, Django, MySQL, Python, Git & GitHub, TypeScript, ReactJS, Astro, Angular, Node.JS, Java, Rust]_
             - Piscina, Acceso al Cursos - :blue[42 Barcelona] _[Agosto 2023 - Enero 2024]_
             _:grey[C, Linux, MSDOS, SOLID, Bases de la programación]_
             - CFGM: Sistemas Microinformáticos y Redes - :blue[IES Lluis Braille] _[Septiembre 2012 - Septiembre 2014]_
             _:grey[Ofimática, Redes, Programación web básica, HTMl, Bases de datos, Linux]_
             - Introducción a la programación e introducción al diseño UX - :blue[Cibernarium, Barcelona Activa] _[2020]_
             _:grey[Programación básica, UI, UX]_
             - Google IT Automation with Python - :red[Google] _[2023]_ :grey[Python, Automation, Testing, Bash Scripting]
             - Introduction to Git and GitHub - :red[Google] _[2023]_ :grey[Git, GitHub]
             - Creación, programación y diseño de páginas web con HTML5 y CSS3 - IFCT031PO - :blue[Grupo Método] _[2024]_ :grey[HTML, HTML5, CSS, JavaScript]
             
             Formación en programación e informática.
             ''')
    st.subheader("Acústica")
    st.write('''
             - Postgrado universitario en Acústica Arquitectónica - :red[Universitat Ramon Llull] _[2020 - 2021]_
             _:grey[Soluciones acústicas, insonorización, acondicionamiento acústico, electroacústica básica]_
             
             Formación en Acústica arquitectónica.
             ''')
    st.subheader("Audio")
    st.write('''
             - CFGS de Sonido para Audiovisuales - :blue[IES Carlos María Rodríguez de Valcárcel] _[Septiembre 2014 - Septiembre 2016]_
             _:grey[Electroacústica básica, edición de audio, sonorización de espectáculos, microfonía, mesas de mezclas, resolución de procesos, radio, TV, doblaje, videojuegos]_
             - Master en postproducción de audio para cine, TV y videojuegos - :violet[Centro de formación CICE Madrid] _[2016 - 2017]_
             _:grey[Edición de audio, diseño sonoro, postproducción, TV, videojuegos, ProTools]_
             - Certificado oficial **Avid ProTools 101 y 130** - :violet[Centro de formación CICE Madrid] _[2016 - 2017]_
             _:grey[Edición de audio, ProTools]_
             
             Formación en Audio Profesional.
             ''')
    st.subheader("Otros")
    st.write('''
             - Master en Marketing Digital y Community Management - :violet[IEBS Biztech School] _[2017 - 2018]_
             _:grey[Marketing digital, publicidad, ventas, RRSS, gestión de marketing]_
             - Especialización en gestión de proyectos de Google - :red[Google] _[2023]_
             _:grey[Kanban, Agile, Project Management, Resolución de problemas, gestión de equipos]_
             
             Formación en diferentes aspectos profesionales como marketing, ventas o gestión de proyectos.
             ''')

with st.expander("Proyectos"):
    tab1, tab2, tab3 = st.tabs(["Mi Web", "QA Tool", "Digital Audio Renamer"])

    with tab1:
        st.write('''
                 Este link te llevará a mi web. En mi web vendo librerías de sonido para UI, UX, también para videojuegos. También comparto mis herramientas, las cuales yo mismo programo. Además hablo de audio, comparto mis conocimientos y te cuento un poco más acerca de mí.
                 ''')
        if st.button("Link a mi web"):
            st.markdown("[Visita mi web](https://digitalaudiotips.com/)", unsafe_allow_html=True)

    with tab2:
        st.write('''
                 Esta herramienta sencilla está diseñada para escuchar audios de los cuales necesitamos comprobar una transcripción. Utiliza un documento de excel como base, y te permite escuchar cada audio individualmente. Si una transcripción no es correcta, podremos modificar el texto directamente en la app.
                 ''')
        if st.button("Link a la app"):
            st.markdown("[Visita mi app](https://github.com/mario-sound/QA_Tool_0.1/)", unsafe_allow_html=True)
    with tab3:
        st.write('''
                 Digital Audio Renamer es una herramienta diseñada para profesionales del sonido, productores de audio y cualquier persona que trabaje con grandes cantidades de archivos de audio. Esta aplicación permite renombrar archivos .wav de forma eficiente, flexible y personalizada, facilitando la organización y el manejo de archivos en proyectos de grabación y edición de sonido.
                 ''')
        if st.button("Link a la app"):
            st.markdown("[Visita mi app](https://github.com/mario-sound/digitalaudiorenamer)", unsafe_allow_html=True)

with st.expander("Idiomas"):
    lan1, lan2, lan3 = st.columns([1,1,1])
    with lan1:
        st.subheader("Español")
        st.write("Idioma nativo")
    with lan2:
        st.subheader("Inglés")
        st.write("Nivel básico profesional")
    with lan3:
        st.subheader("Catalán")
        st.write("Competencia básica")

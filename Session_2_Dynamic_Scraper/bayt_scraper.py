from playwright.sync_api import sync_playwright  # Importer Playwright pour contrôler le navigateur
from bs4 import BeautifulSoup  # Importer BeautifulSoup pour analyser le HTML

with sync_playwright() as p:  # Démarrer Playwright
    Baseurl = "https://www.bayt.com/en/tunisia/jobs/"  # URL de la page des emplois en Tunisie
    browser = p.chromium.launch(headless=False)  # Ouvrir le navigateur (Headless = non affichage du navigateur)
    page = browser.new_page()  # Créer une nouvelle page/onglet
    page.goto(Baseurl)  # Aller à la page des emplois

    jobs = page.locator("li[class*='has-pointer-d']")  # Localiser toutes les offres d'emploi
    print(f"{jobs.count()} job listings")  # Afficher le nombre d'emplois trouvés

    links = []  # Liste pour stocker les liens des emplois
    for i in range(jobs.count()):  # Parcourir chaque emploi trouvé
        job = jobs.nth(i)  # Prendre le i-ème emploi
        href = job.locator("a[data-js-aid='jobID']").get_attribute("href")  # Extraire le lien de l'emploi
        if href:  # Si le lien existe
            href = "https://www.bayt.com" + href  # Créer l'URL complète
            links.append(href)  # Ajouter le lien à la liste

    for link in links :  # Parcourir chaque lien d'emploi
        page = browser.new_page()  # Ouvrir une nouvelle page
        page.goto(link)  # Aller à la page de l'emploi
        soup = BeautifulSoup(page.content(), "html.parser")  # Analyser le HTML de la page
        job_container = soup.find("div", {"id" : "job_card"})  # Trouver le conteneur principal de l'emploi

        if job_container:  # Si le conteneur existe
            title_elem = job_container.find("h1", id="job_title")  # Chercher le titre de l'emploi
            title = title_elem.text.strip() if title_elem else "N/A"  # Extraire le titre ou mettre N/A si absent

            company_elem = job_container.find("ul", {"class" : "list is-basic"})  # Chercher les infos de l'entreprise ( ou bien .find("ul" , class_="list is-basic")
            company_name = company_elem.find("li").text.strip() if company_elem and company_elem.find("li") else "N/A"  # Extraire le nom de l'entreprise

            post_date_elem = job_container.find("span", id="jb-posted-date")  # Chercher la date de publication
            post_date = post_date_elem.text.strip() if post_date_elem else "N/A"  # Extraire le texte de la date

            experience_elem = job_container.find("div", {"data-automation-id":"id_type_level_experience"})  # Chercher l'expérience requise
            experience = experience_elem.text.strip() if experience_elem else "N/A"  # Extraire le texte de l'expérience

            job_description_elem = job_container.find("div", {"class" : "t-break"})  # Chercher la description de l'emploi
            if job_description_elem:  # Si la description existe
                job_description = job_description_elem.get_text(separator="\n", strip=True)  # Extraire tout le texte avec retours à la ligne
                # on a utilise get_text car dans le div ilya plusiers balise <p> et <br> pour separer les paragraphes
            else:  # Sinon
                job_description = "N/A"  # Mettre N/A

            print(f"Title: {title}")  # Afficher le titre
            print(f"Company: {company_name}")  # Afficher le nom de l'entreprise
            print(f"Post Date: {post_date}")  # Afficher la date de publication
            print(f"Experience: {experience}")  # Afficher l'expérience requise
            print(f"Description: {job_description}")  # Afficher la description
            print("-" * 50)  # Afficher une ligne de séparation

        page.close()  # Fermer la page après traitement

    browser.close()  # Fermer le navigateur


# À compléter : ajouter chaque élément dans une liste de dictionnaires et l'exporter en CSV ou Excel
# Utiliser la bibliothèque pandas
# import pandas as pd

# on a utilise if ... else "N/A" pour assurer que le code ne plante pas si il manque un élément dans la page de l'emploi

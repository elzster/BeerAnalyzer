# <p align="center"> Project 3 - Beer Me...Something Different! </p>

### <p align="center"> Beer Recommender Engine & Sentiment Analysis on Reviews </p>

The Team : <details>
           <summary>Beer Analysts + LinkedIn Profiles: </summary>
           <p> </p>
           <p> :large_orange_diamond: [Christine Mazur](https://www.linkedin.com/in/christine-mazur-4b897425/) - IT Project Manager</p>
           <p> :large_orange_diamond: [Elie Hakim](https://www.linkedin.com/in/hakime1/) - Data Analyst </p>
           <p> :large_orange_diamond: [Jean Pino](https://www.linkedin.com/in/jeancpino/) - Data Analyst </p>
           <p> :large_orange_diamond: [Jonathan Rinko](https://www.linkedin.com/in/jonathan-rinko/) - Data Analyst</p>
           <p> :large_orange_diamond: [Miguel Patxot](https://www.linkedin.com/in/mpatxot/) - Data Analyst </p>
           <p> :large_orange_diamond: [Nida Hussain](https://www.linkedin.com/in/nida-hussain-0b009932/) - Software Partners Operations Specialist</p>
         </details>

![header image](https://anigamers.com/uploads/entries/Bartender2_20150404224430.jpg)

### |-----------------------------------------------------------------------------------------|
### :beer: Bartender: What would you like to drink today?
### :mushroom: You: Not sure honestly...I've been drinking the same beer for quite some time; I want to try something new today...
### :beer: Bartender: That's perfect! Take a look at our 'Beer Analyzer App'; I'm sure you can find a possibility of information and new choices based on what you already like!
### |-----------------------------------------------------------------------------------------|

# <p align="center"> Welcome to the 'Beer Analyzer App'! </p>
![header image](/beer/readme_images/welcome_page.png)

# <p align="center"> Our Mission </p>
![header image](/beer/readme_images/our_mission_.png)

# <p align="center"> Data Process | Clean Up </p>
![header image](/beer/readme_images/data_process.png)

# <p align="center"> Beer Review - Sentiment Analysis </p>
VADER - Valence Aware Dictionary for sEntiment Reasoning
* 'Opinion Mining' or 'Quantifying the Emotion of a Word' 
* Approximately 10k individual reviews web scraped using beautiful soup from 'Ratebeer.com' 
* Objective is to compare review sentiment with actual rating provided by same users which rates each beer from 0-5.
![header image](/beer/readme_images/vader_top.png)
![header image](/beer/readme_images/vader_geo.png)

# <p align="center"> Beer Recommender Engine </p>
![header image](/beer/readme_images/recommender_v2.png)

This beer recommendation engine is built on collaborative-filtering approach. Since the review-rating matrix is very sparse, cosine similarity was suitable to calculate similarities between beers. This app recommends top 5 beers by taking user inputs and comparing against this pre-computed matrix. 

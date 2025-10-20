# IngrediGenie

### Problem & Inspiration
Inspired by the global issue of food waste, IngrediGenie was created to tackle the common problem of unused ingredients in home kitchens. I was motivated to build a solution that helps individuals reduce waste and save money by making creative, delicious meals out of what they already have. The goal is to turn a problem into a creative opportunity.

### Solution
IngrediGenie is a full-stack web application powered by Python's Flask framework and the OpenAI API Users simply input a list of ingredients, and the platform dynamically generates a unique, customized recipe for them. This AI-driven approach eliminates the need for manual recipe searching and provides an instant, personalized cooking solution.

### Future Improvements
Looking ahead, I plan to enhance IngrediGenie with several key features. This includes adding user accounts to allow for saving favorite recipes, integrating an image generation API to provide a visual of the final dish, and incorporating user feedback to refine the recipe generation process for even more creative and practical results.

### What I Learned
Building IngrediGenie was a valuable learning experience that reinforced my understanding of several key technologies. I gained hands-on experience with the Flask framework, front-end development (HTML, CSS, and JavaScript), and responsive design. I also learned to implement smooth-scrolling navigation and dynamic, scroll-based animations using the Intersection Observer API for a better user experience.

### How I Built It
I began by designing the main user flow: a home page to introduce the concept and a separate page for recipe generation. I used HTML to structure both pages, linking them together through navigation and a call-to-action button. The visual identity was established in styles.css with a color scheme of warm oranges, yellows, and reds to create an inviting atmosphere. On the back-end, app.py was set up to handle the routing and serve the static files and templates. The interactive elements, such as the FAQ dropdown and scroll animations, were implemented using JavaScript.

### Challenges I Faced
The most significant challenge I encountered was getting the output from the OpenAI API to dynamically update in the HTML. The Flask back-end successfully called the API and received the recipe data, but I struggled to pass this data to the front-end and render it in real-time without a full page reload. This required me to use JavaScript's Fetch API to make an asynchronous request to the Flask back-end. I then had to write a JavaScript function to parse the JSON response from the server and dynamically create the HTML elements for the recipe card. Debugging the asynchronous calls and ensuring that the generated HTML was correctly formatted and injected into the DOM was a complex but ultimately rewarding task.

### Accomplishments That I'm Proud Of
I am most proud of successfully integrating the front-end and back-end to create a seamless, dynamic user experience. The asynchronous communication between the JavaScript front-end and the Flask back-end, powered by the OpenAI API, was a complex challenge that I successfully overcame. I am also proud of the clean, professional design of the website, including the scroll animations and interactive FAQ section, which I was able to build entirely on my own.


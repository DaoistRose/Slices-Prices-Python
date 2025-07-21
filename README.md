# Slices-Prices-Python

**My Beginner’s Journey (Part 3)**

Len’s Slices 4 Mices is a small but mighty pizza shop serving up slices for every craving. My latest Codecademy Python 3 project brought me into the world of menu management. The task? Take a simple list of toppings and prices, and transform them into a sortable, structured menu that could be updated, sliced, and displayed to customers.

This project gave me a chance to go deeper into lists, tuples, sorting, and data validation. While the initial instructions were straightforward, I found plenty of room to play, polish, and reflect along the way.

---

## Getting Started

I’m continuing my beginner Python journey (Day 6), and with each new project, I’m starting to notice a shift in how I approach code. This time, Codecademy asked me to build a pizza menu manager—a program that stores prices and toppings, sorts them by cost, and identifies the cheapest and priciest slices.

While this wasn’t as logic-heavy as shipping calculations or input validation, it gave me hands-on practice with organizing and pairing data in a meaningful way. There was a clear path laid out, but I also saw many little places to add safety checks and flavor (pun intended).

---

### Project Overview

The core of this project was to create and manage a pizza menu. I started by creating two lists: one for toppings and one for their corresponding prices. Then, I combined them into a two-dimensional list where each item had the price first and the topping second.

Once the menu was created, I sorted it by price to identify the cheapest and most expensive slices. I then removed the last slice of anchovies from the list and added a new item: peppers at $2.50 per slice. Finally, I grabbed the three cheapest slices to create a little deal for our imaginary customers.

---

### Starting Points

- Create a list of toppings and a corresponding list of prices  
- Count the number of $2 slices using `.count()`  
- Calculate the total number of pizza types with `len()`  
- Pair each price with its topping using `zip()` and convert it to a list  
- Sort the list by price  
- Remove the priciest item, add a new one, and ensure the list remains sorted  
- Slice the list to get the three cheapest pizzas  

Once I had all of this working, I started asking myself what could go wrong, and how to make the experience more complete.

---

## Enhancing the Experience

### Data Integrity Checks

I began by checking if the original toppings or prices lists were empty. It wasn’t required by the assignment, but it felt important to build in a simple fail-safe. I also made sure each topping had a price after combining the data, which helped prevent formatting errors later.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/lkw1zhvi15nhz2re8xfp.png)

### Discovering zip()

One of my favorite discoveries in this project was using zip() to pair prices with their corresponding toppings. I initially considered matching them manually, but zip() made it both faster and cleaner. Once zipped, I converted the result into a list using list() so I could sort, modify, and work with the data more flexibly. It felt like unlocking a new Python shortcut that I’ll definitely reuse in future projects.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/sq4cndvnw5hw0abqh4tn.png)

### Replacing Anchovies

When the anchovies sold out, I removed them from the list and added peppers instead. I learned that inserting a new item into a sorted list requires a fresh sort to maintain order. That small realization made me appreciate the need for clean, consistent data flow.

### Formatted Output

I printed the menu line by line using formatted strings, which was a good exercise in handling nested data. I didn’t use a loop this time because I wanted to keep my focus on tuple structure and formatting logic. It was a bit repetitive, but seeing it play out helped me understand how each element fits together.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nse0r1c8jhdgywhdfcic.png)

### Daily Special

I had some fun with the “Three Blind Mice” idea—bundling our three cheapest pizzas into a special deal. This approach didn’t change the core logic of the program but made the output feel more polished and personal, giving customers a unique, catchy offer to look forward to.

One important detail was adding a safety check to ensure the special only appears when we actually have enough pizzas available. Since the special requires three different pizza options, I implemented a condition to simulate inventory availability and prevent errors that would occur if there are fewer than three pizzas to choose from.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/tcopeu5mx9bihzh15b6c.png)

---

## Lessons Learned

This project helped me solidify a few key concepts:

- Pairing data using `zip()` is simple and powerful  
- Sorting a list of tuples is surprisingly effective and easy to use  
- Removing and adding data requires thoughtful restructuring if you care about order  
- Sometimes it’s okay to avoid loops if you’re focusing on learning another concept  
- Even a static menu can be a great place to practice validation and formatting  

---

## Final Thoughts

This was a smaller project compared to my previous two, but it introduced important ideas that build the foundation for more advanced data handling. It made me think more about how to structure and present information, and it reminded me that even basic logic needs guardrails to work reliably.

Next, I’d love to refactor the print statements into a loop, then begin wrapping things into functions. Eventually, I want to build a version where users can “order” pizzas or update the menu on the fly.

For now, I’m happy that the menu works, the logic holds up, and I got to practice making my code both functional and a little bit fun.

---

Thanks for reading! If you’re also working through Codecademy’s Python curriculum, feel free to share your version or your take on this project. Let's keep learning together!

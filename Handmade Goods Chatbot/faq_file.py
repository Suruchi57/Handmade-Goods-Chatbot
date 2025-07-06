import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")

# Sample FAQs for handmade goods
faqs = [
    {"question": "What materials are used in your handmade products?",
     "answer": "We use eco-friendly, high-quality materials like cotton, wood, clay, soy wax, and natural beads."},

    {"question": "Do you offer custom or personalized items?",
     "answer": "Yes! Many of our items like jewelry, mugs, and cards can be personalized. Just leave a note at checkout."},

    {"question": "How long does shipping take?",
     "answer": "Shipping typically takes 5-7 business days within the country."},

    {"question": "Do you ship internationally?" or "Where do ypu sell the items?",
     "answer": "Yes, we offer worldwide online shipping with delivery in 10-15 business days."},

    {"question": "What payment methods do you accept?",
     "answer": "We accept payments via PayPal, Credit Card, Apple Pay, and Google Pay."},

    {"question": "Can I return or exchange items?",
     "answer": "Yes, returns and exchanges are accepted within 14 days of delivery, except for custom orders."},

    {"question": "How can I track my order?",
     "answer": "You will receive a tracking link via email once your order has shipped."},

    {"question": "What kind of handmade products do you sell?",
     "answer": "We sell candles, cardboard crafts, hand-painted mugs, handmade jewelry, home decors, cardboard desk calendar, and greeting cards."},

    {"question": "Are your candles scented?",
     "answer": "Yes, our candles are made with natural soy wax and infused with essential oil scents like lavender, vanilla, and citrus."},

    {"question": "Can I request a custom design on a mug?",
     "answer": "Absolutely! You can request custom names, quotes, or artwork on our ceramic mugs."},

    {"question": "Do you have gift wrapping options?",
     "answer": "Yes, gift wrapping is available at checkout for a small additional fee."},

    {"question": "How do I care for handmade pottery?",
     "answer": "Our pottery is dishwasher and microwave safe, but hand washing is recommended to preserve the finish."}
]

# Casual message replies (non-FAQ intent)
casual_responses = {
    "ok": "Got it!",
    "okay": "Alright!",
    "thanks": "You're welcome!",
    "thank you": "Happy to help!",
    "cool": "😎",
    "great": "Glad you think so!",
    "awesome": "Yay! 😊",
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! Feel free to ask me anything about our handmade products.",
    "bye": "Goodbye! Thanks for visiting our handmade shop."
}

# Extract FAQ questions
questions = [faq["question"] for faq in faqs]

# TF-IDF vectorizer for converting text to vectors
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(questions)

# Function to get chatbot response
def get_response(user_input):
    lower_input = user_input.strip().lower()

    # Check for casual message
    if lower_input in casual_responses:
        return casual_responses[lower_input]

    # Otherwise, do FAQ matching
    user_vector = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vector, faq_vectors)
    best_match = similarity.argmax()
    score = similarity[0][best_match]

    if score > 0.3:
        return faqs[best_match]["answer"]
    else:
        return "Sorry, I couldn't understand your question. Please try rephrasing it."

# Chatbot loop
def chat():
    print("Handmade Goods FAQ Chatbot 🤖 (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Thanks for visiting our handmade shop! 🧵")
            break
        response = get_response(user_input)
        print("Bot:", response)

# Run the chatbot
if __name__ == "__main__":
    chat()

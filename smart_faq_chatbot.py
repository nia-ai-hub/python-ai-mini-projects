
from sentence_transformers import SentenceTransformer, util

# Questions and answers for our FAQ chatbot
faqs = [
    {
        "question": "How do I register on the website?",
        "answer": "To register, open the registration page and fill out the required information."
    },
    {
        "question": "How can I change my password?",
        "answer": "Go to your account settings and select the Change Password option."
    },
    {
        "question": "How can I contact customer support?",
        "answer": "Visit the Contact Us page and send a message to the support team."
    },
    {
        "question": "Where can I find the courses?",
        "answer": "Go to the Courses page to see all available training courses."
    },
    {
        "question": "Are the courses free?",
        "answer": "The price of each course is listed on its course page."
    },
    {
        "question": "What should I do if I forget my password?",
        "answer": "On the login page, select the Forgot Password option."
    },
    {
        "question": "How can I create an account?",
        "answer": "Click Register and enter the required information to create your account."
    },
    {
        "question": "How do I log out of my account?",
        "answer": "Open the account menu and select the Log Out option."
    },
]

print("Loading the AI model...")

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

# Convert FAQ questions into embeddings
faq_questions = [faq["question"] for faq in faqs]

faq_embeddings = model.encode(
    faq_questions,
    convert_to_tensor=True,
    normalize_embeddings=True
)

print("\nChatbot is ready!")
print("Ask me anything about our services.")
print("Press ENTER without typing a question to exit.")

while True:
    user_question = input("\nYour question: ").strip()

    # Exit when the user presses ENTER without typing anything
    if not user_question:
        print("Goodbye!")
        break

    # Convert the user's question into an embedding
    question_embedding = model.encode(
        user_question,
        convert_to_tensor=True,
        normalize_embeddings=True
    )

    # Compare the user's question with FAQ questions
    similarities = util.cos_sim(
        question_embedding,
        faq_embeddings
    )[0]

    best_index = int(similarities.argmax().item())
    best_score = float(similarities[best_index].item())

    # Return the closest answer if similarity is high enough
    if best_score >= 0.45:
        print("\nAnswer:", faqs[best_index]["answer"])
        print(f"Similarity score: {best_score:.2f}")
    else:
        print("\nSorry, I couldn't find a suitable answer.")
        print("Please try asking in a different way.")

from sentence_transformers import SentenceTransformer, util

# Questions and answers for our FAQ chatbot
faqs = [
    {
        "question": "How do I register on the website?",
        "answer": "To register, open the registration page and fill out the required information."
    },
    {
        "question": "How can I change my password?",
        "answer": "Go to your account settings and select the Change Password option."
    },
    {
        "question": "How can I contact customer support?",
        "answer": "Visit the Contact Us page and send a message to the support team."
    },
    {
        "question": "Where can I find the courses?",
        "answer": "Go to the Courses page to see all available training courses."
    },
    {
        "question": "Are the courses free?",
        "answer": "The price of each course is listed on its course page."
    },
    {
        "question": "What should I do if I forget my password?",
        "answer": "On the login page, select the Forgot Password option."
    },
    {
        "question": "How can I create an account?",
        "answer": "Click Register and enter the required information to create your account."
    },
    {
        "question": "How do I log out of my account?",
        "answer": "Open the account menu and select the Log Out option."
    },
]

print("Loading the AI model...")

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

# Convert FAQ questions into embeddings
faq_questions = [faq["question"] for faq in faqs]

faq_embeddings = model.encode(
    faq_questions,
    convert_to_tensor=True,
    normalize_embeddings=True
)

print("\nChatbot is ready!")
print("Ask me anything about our services.")
print("Press ENTER without typing a question to exit.")

while True:
    user_question = input("\nYour question: ").strip()

    # Exit when the user presses ENTER without typing anything
    if not user_question:
        print("Goodbye!")
        break

    # Convert the user's question into an embedding
    question_embedding = model.encode(
        user_question,
        convert_to_tensor=True,
        normalize_embeddings=True
    )

    # Compare the user's question with FAQ questions
    similarities = util.cos_sim(
        question_embedding,
        faq_embeddings
    )[0]

    best_index = int(similarities.argmax().item())
    best_score = float(similarities[best_index].item())

    # Return the closest answer if similarity is high enough
    if best_score >= 0.45:
        print("\nAnswer:", faqs[best_index]["answer"])
        print(f"Similarity score: {best_score:.2f}")
    else:
        print("\nSorry, I couldn't find a suitable answer.")
        print("Please try asking in a different way.")
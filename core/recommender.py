from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from core.models import Product


class ContentBasedRecommender:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.similarity_matrix = None
        self.products = None

    def fit(self):
        products = Product.objects.all()
        description = [product.description for product in products]
        self.products = [product.pid for product in products]
        tfidf_matrix = self.vectorizer.fit_transform(description)
        self.similarity_matrix = cosine_similarity(tfidf_matrix)

    def recommend(self, pid, num_recommendations=5):
        product_index = self.products.index(pid)
        similarity_scores = list(enumerate(self.similarity_matrix[product_index]))
        similarity_scores.sort(key=lambda x: x[1], reverse=True)
        recommendations = similarity_scores[
            1 : num_recommendations + 1
        ]  # Exclude the product itself
        return recommendations
        # print(recommendations)

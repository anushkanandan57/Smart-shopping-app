import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load sample product dataset (You can replace it with real data)
product_data = {
    'product_id': [1, 2, 3, 4, 5],
    'product_name': ['Shoes', 'T-Shirt', 'Jeans', 'Watch', 'Backpack'],
    'category': ['Fashion', 'Fashion', 'Fashion', 'Accessories', 'Accessories'],
    'price': [2000, 500, 1200, 3000, 1500]
}
products_df = pd.DataFrame(product_data)

# Sample user purchase history (Simulating a small dataset)
user_data = {
    'user_id': [101, 102, 103, 104],
    'purchased_product_id': [[1, 2], [3, 5], [1, 4], [2, 3, 5]]
}
users_df = pd.DataFrame(user_data)

# Function to recommend products based on past purchases
def recommend_products(user_id):
    # Find the user's past purchases
    user_row = users_df[users_df['user_id'] == user_id]
    if user_row.empty:
        return "No purchase history found!"
    
    purchased_products = user_row.iloc[0]['purchased_product_id']
    
    # Find products in the same category
    recommended_products = products_df[~products_df['product_id'].isin(purchased_products)]
    
    return recommended_products[['product_id', 'product_name', 'category']]

# Test recommendation function
if __name__ == "__main__":
    test_user_id = 101  # Change this to test different users
    print(recommend_products(test_user_id))

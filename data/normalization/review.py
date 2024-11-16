def normalize_review(review: str):
    if review is None:
        return None

    # Strip the space between the number of reviews "4.6 (204)" and takes the review only.
    review = review.split(' ')[0]
    review_number = float(review)
    return review_number

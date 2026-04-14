function toggleReviewForm() {
  const form = document.getElementById("reviewFormContainer");
  form.style.display = form.style.display === "none" ? "block" : "none";
}

function toggleCommentForm(reviewId) {
  const form = document.getElementById("commentForm-" + reviewId);
  form.style.display = form.style.display === "none" ? "block" : "none";
}
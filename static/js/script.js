// Form Toggles

// Review Form Toggle
function toggleReviewForm() {
  const form = document.getElementById("reviewFormContainer");
  form.style.display = form.style.display === "none" ? "block" : "none";
}

// Comment Form Toggle
function toggleCommentForm(reviewId) {
  const form = document.getElementById(`commentForm-${reviewId}`);
  form.style.display = form.style.display === "none" ? "block" : "none";
}

// Edit Review Form Toggle
function toggleEditReviewForm(reviewId) {
  const form = document.getElementById(`editReviewForm-${reviewId}`);

  if (form.style.display === "none") {
    // Pre-populate fields from data attributes on the card
    const card = document.querySelector(`[data-review-id="${reviewId}"]`);
    form.querySelector('[name="title"]').value = card.dataset.reviewTitle;
    form.querySelector('[name="content"]').value = card.dataset.reviewContent;
    form.querySelector('[name="rating"]').value = card.dataset.reviewRating;
    form.style.display = "block";
  } else {
    form.style.display = "none";
  }
}

// Edit Comment Form Toggle
function toggleEditCommentForm(commentId) {
  const form = document.getElementById(`editCommentForm-${commentId}`);

  if (form.style.display === "none") {
    const card = document.querySelector(`[data-comment-id="${commentId}"]`);
    form.querySelector('[name="content"]').value = card.dataset.commentContent;
    form.style.display = "block";
  } else {
    form.style.display = "none";
  }
}

// Delete Comment Modal
function openDeleteCommentModal(commentId) {
  document.getElementById("deleteCommentForm").action =
    `/comments/${commentId}/delete/`;

  const modal = new bootstrap.Modal(
    document.getElementById("deleteCommentModal"),
  );
  modal.show();
}

// Delete Review Modal
function openDeleteModal(reviewId, reviewTitle) {
  document.getElementById("deleteReviewTitle").textContent = reviewTitle;
  document.getElementById("deleteReviewForm").action =
    `/reviews/${reviewId}/delete/`;
  const modal = new bootstrap.Modal(
    document.getElementById("deleteReviewModal"),
  );
  modal.show();
}

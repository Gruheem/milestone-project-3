console.log("JS file loaded");

// Remove Focus on Nav Toggler After Collapsing
document.querySelector('.navbar-toggler').addEventListener('click', function() {
  if (this.classList.contains('collapsed')) {
    this.blur();
  }
});

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

// Delete Library Entry Modal
function openDeleteLibraryModal(entryId, gameTitle) {
  document.getElementById('deleteLibraryTitle').textContent = gameTitle;
  document.getElementById('deleteLibraryForm').action = `/library/remove/${entryId}/`;
  const modal = new bootstrap.Modal(document.getElementById('deleteLibraryModal'));
  modal.show();
}

// Log Session Form Toggle
function toggleSessionForm() {
  const form = document.getElementById("sessionFormContainer");
  form.style.display = form.style.display === "none" ? "block" : "none";
}

// Delete Session Modal
function openDeleteSessionModal(entryId, sessionId) {
  document.getElementById("deleteSessionForm").action = `/library/${entryId}/sessions/delete/${sessionId}/`;
  const modal = new bootstrap.Modal(document.getElementById("deleteSessionModal"));
  modal.show();
}

// Edit Session Form Toggle
function toggleEditSessionForm(sessionId) {
  const form = document.getElementById(`editSessionForm-${sessionId}`);

  if (form.style.display === "none" || form.style.display === "") {

    // get card data
    const card = document.querySelector(`[data-session-id="${sessionId}"]`);

    // IMPORTANT: crispy uses id_... not name selectors reliably
    form.querySelector('[name="notes"]').value = card.dataset.sessionNotes || "";
    form.querySelector('[name="date_played"]').value = card.dataset.sessionDate || "";
    form.querySelector('[name="duration"]').value = card.dataset.sessionDuration || "";
    form.querySelector('[name="first_place"]').value = card.dataset.sessionFirstPlace || "";
    form.querySelector('[name="second_place"]').value = card.dataset.sessionSecondPlace || "";
    form.querySelector('[name="third_place"]').value = card.dataset.sessionThirdPlace || "";

    form.style.display = "block";

  } else {
    form.style.display = "none";
  }
}
$(document).ready(function () {
  function getPostSection(el) {
    return el.closest("section[data-post-id]");
  }

  $(".edit-post-btn").click(function () {
    const postSection = getPostSection($(this));

    const postBody = postSection.find(".post-body")
    postBody.addClass("d-none");

    const postEditForm = postSection.find(".edit-post-form");
    postEditForm.find("textarea").val(postBody.text());
    postEditForm.removeClass("d-none");
  });

  $(".cancel-edit-post-btn").click(function () {
    const postSection = getPostSection($(this));
    postSection.find(".edit-post-form").addClass("d-none");
    postSection.find(".post-body").removeClass("d-none");
  });
});

//-------------------------------------------------------------------------------------------------------------------------------------

// Chat when clicked marked unread
function markRead() {
    document.getElementById("sojuChat").innerHTML = "";
}

//-------------------------------------------------------------------------------------------------------------------------------------

// Edit button toggle to Submit button - SOURCE: https://codepen.io/html5andblog/pen/BpzvZW
var clickState = 0;
var btn = document.getElementById("editButton");
btn.addEventListener('click', function(){

  if (clickState == 0) {
    // Editable State - To Submit
    this.textContent = 'Submit';
    clickState = 1;
    document.getElementById("onlyView").removeAttribute("readonly");

  } else {
    // Non-editable State - To Edit
    this.textContent = 'Edit';
    clickState = 0;
    document.getElementById("onlyView").setAttribute("readonly", true);

    var x = document.lastModified;
    document.getElementById("lastEdited").innerHTML = "Last Submitted: " + x;
  }
});
// END SOURCE

//-------------------------------------------------------------------------------------------------------------------------------------

// My Solution Tab: Post Confirm Function 
function postConfirm() {
    var confirmStatus = confirm("Are you sure you'd like to post your comment?");
    if (confirmStatus == true) {
        post();
        notify();
    } 
}

// My Solution Tab: Post Name & Comment to Thread
function post() {
    person = document.getElementById("postName");
    sessionStorage.setItem("postName", person.value);

    feedback = document.getElementById("postFeedback");
    sessionStorage.setItem("postFeedback", feedback.value);

    document.getElementById("personImg").innerHTML = '<img class="d-flex mr-3 rounded-circle" src="http://placehold.it/50x50" alt="">';
    document.getElementById('threadName').innerHTML = sessionStorage.getItem('postName');
    document.getElementById('thread').innerHTML = sessionStorage.getItem('postFeedback');
    document.getElementById('newReply').innerHTML = "Reply";

    // To empty fields after submission
    document.getElementById("postName").value = "";
    document.getElementById("postFeedback").value = "";
}

//-------------------------------------------------------------------------------------------------------------------------------------

// Anin Solution: Post Confirm Function 
function aninPostConfirm() {
    var confirmStatus = confirm("Are you sure you'd like to post your comment?");
    if (confirmStatus == true) {
        aninPost();
        notify();
    } 
}

// Anin Solution: Tab: Post Name & Comment to Thread
function aninPost() {
    person = document.getElementById("anin-postName");
    sessionStorage.setItem("anin-postName", person.value);

    feedback = document.getElementById("anin-postFeedback");
    sessionStorage.setItem("anin-postFeedback", feedback.value);

    document.getElementById("anin-personImg").innerHTML = '<img class="d-flex mr-3 rounded-circle" src="http://placehold.it/50x50" alt="">';
    document.getElementById('anin-threadName').innerHTML = sessionStorage.getItem('anin-postName');
    document.getElementById('anin-thread').innerHTML = sessionStorage.getItem('anin-postFeedback');
    document.getElementById('anin-newReply').innerHTML = "Reply";

    // To empty fields after submission
    document.getElementById("anin-postName").value = "";
    document.getElementById("anin-postFeedback").value = "";
}

//-------------------------------------------------------------------------------------------------------------------------------------

// Reply to Feedback
$('.reply-button').click(function(){
    $(this).after($('<textarea>').attr('class','reply-box'));
  });

//-------------------------------------------------------------------------------------------------------------------------------------

// Feedback Notification
function notify() {
    var curr = +document.getElementById("notifyNew").innerHTML;
    document.getElementById("notifyNew").innerHTML = curr + 1;
}

//-------------------------------------------------------------------------------------------------------------------------------------
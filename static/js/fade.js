document.addEventListener('DOMContentLoaded', function() {
  const img1 = document.getElementById('image1');
  const img2 = document.getElementById('image2');
  document.querySelector('.navbar-brand').addEventListener('click', function(e) {
    e.preventDefault();
    img1.classList.add('active');
    img2.classList.remove('active');
    setTimeout(() => {
      img1.classList.remove('active');
      img2.classList.add('active');
    }, 5000);
  });
});

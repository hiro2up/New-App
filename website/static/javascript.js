
// const small = document.getElementById("small"),
// 	medium = document.getElementById("medium"),
// 	large = document.getElementById("large"),
// 	xlarge = document.getElementById("xlarge");


// small.addEventListener("change", function(){
// 	document.getElementById("total-amount").value = "€ 70";
// })

// medium.addEventListener("change", function(){
// 	document.getElementById("total-amount").value = "€ 100";
// })

// large.addEventListener("change", function(){
// 	document.getElementById("total-amount").value = "€ 140";
// })

// xlarge.addEventListener("change", function(){
// 	document.getElementById("total-amount").value = "€ 200";
// })

// function toggle(){
//   var toggling = document.getElementById('shipping-block');
//   if (toggling.style.display == 'none'){
//     toggling.style.display == 'block'
//   }
//   else{
//     toggling.style.display == 'none'
//   }
// }

function toggle(divId, element)
{
    document.getElementById(divId).style.display = element.value == 'No' ? 'block' : 'none';
}




let orderForm = document.getElementById("order-form");
for (var i = 0; i < orderForm.length; i++) {
  if (orderForm[i].type === 'radio') {
    orderForm[i].addEventListener('change', function() {
      totalAmount();
    });
  }
}

function totalAmount() {
  let sum = 0;
  let myTotal = document.getElementById('total-amount');

  for (var i = 0; i < orderForm.length; i++) {
    if (orderForm[i].type === 'radio' && orderForm[i].checked) {
      sum += parseInt(orderForm[i].value, 10);
      myTotal.value = "€ " + sum.toString();
    }
  }
}
// Checkbox toggle function - Orders page
function toggle(divId, element)
{
    document.getElementById(divId).style.display = element.value == 'No' ? 'block' : 'none';

    if (document.getElementById('shipping-option').value == 'Yes'){
      document.getElementById('ship-addr1').required = false
      document.getElementById('ship-addr2').required = false
      document.getElementById('ship-addr3').required = false
      document.getElementById('ship-addr4').required = false
    }
    else{
      document.getElementById('ship-addr1').required = true
      document.getElementById('ship-addr2').required = true
      document.getElementById('ship-addr3').required = true
      document.getElementById('ship-addr4').required = true
    }
}


// Calculating total amount - Orders page
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
  let myTotal = 0;

  for (var i = 0; i < orderForm.length; i++) {
    if (orderForm[i].type === 'radio' && orderForm[i].checked) {
      sum += parseInt(orderForm[i].value, 10);
    
      myTotal = "€ " + sum.toString();
    }
  }
  document.getElementById('total-amount').value = myTotal;
}

//My Account Update Info
function updShow(){
  document.getElementById('upd-buttons').style.display = 'block'

  document.getElementById('upd-firstName').readOnly = false
  document.getElementById('upd-lastName').readOnly = false
  document.getElementById('upd-addrline1').readOnly = false
  document.getElementById('upd-addrline2').readOnly = false
  document.getElementById('upd-city').readOnly = false
  document.getElementById('upd-eircode').readOnly = false
  
}

function updHide(){
  document.getElementById('upd-buttons').style.display = 'none'

  document.getElementById('upd-firstName').readOnly = true
  document.getElementById('upd-lastName').readOnly = true
  document.getElementById('upd-addrline1').readOnly = true
  document.getElementById('upd-addrline2').readOnly = true
  document.getElementById('upd-city').readOnly = true
  document.getElementById('upd-eircode').readOnly = true
}
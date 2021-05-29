// Checkbox toggle function - Orders page
// On order page, depending on the shipping address selection (same as account or different address), the fields will be required or not
// If the same as account, those fields will not be required and hidden as the info will be taken from database
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

/////////////////////////////////////////////////////////////////////////////////////////////
// Calculating total amount - Orders page
// Taken from https://stackoverflow.com/questions/57751078/how-to-get-the-sum-of-items-selected-in-javascript-with-radio-buttons
// This piece of code iterates through all the radio input type fields in the form and sums up all values to give the total, which will be included in the order.
// Each time you select a different option, the totalAmount function is triggered and the total is calculated
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

//////////////////////////////////////////////////////////////////////
//My Account Update Info
// It changes the readonly status for the account info fields, allowing the info to be updated. The changes are based on "Edit" and "Cancel" buttons on the page
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
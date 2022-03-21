function getdinner(date) {
    clickeddate = date
    var modal = $('#Dinnermodal');
    var url = modal.attr('geturl');
    $.ajax({
        url: url,
        data: {
            'date': date,
        },
        success: function (data) {
            modal.find('.modal-body').html(data);
            modal.find('.modal-title').text(date + ' Dinner');
            modal.modal('show');
        }
    });
};

function rollthedice() {
    document.getElementById('dicespinner').style.display = 'block';
    var modal = $('#Dinnermodal');
    var url = modal.attr('rollurl');
    $.ajax({
        url: url,
        success: function (data) {
            modal.find('.dinner-body').html(data);
            document.getElementById('dicespinner').style.display = 'none';
        }
    });
};

function selectdinner() {
    var modal = $('#Dinnermodal');
    var url = modal.attr('selecturl');
    $.ajax({
        url: url,
        data:{
            'dinner_id': $('#selectdinner').val(),
        },
        success: function (data) {
            modal.find('.dinner-body').html(data);
        }
    });
};  

//create date model
function savedinner() {
    var modal = $('#Dinnermodal');
    var url = modal.attr('saveurl');
    $.ajax({
        url: url,
        data:{
            'dinnerID': $('#dinnerID').val(),
            'random': $('#dinnerType').val(),
            'dinnerDescription': $('#dinnerDescription').val(),
            'dinnerIngredient': $('#dinnerIngredient').val(),
            'dinnerMeasurement': $('#dinnerMeasurement').val(),
            'dinnerDate': clickeddate,
            'dinnerDish': $('#dinnerDish').html(),
        },
        success: function (data) {
            console.log(data)
            if (data = 'Success'){
                modal.modal('hide'); 
                calendaritem.refetchEvents();
            };
        }
    });
};  
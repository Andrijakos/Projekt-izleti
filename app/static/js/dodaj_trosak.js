
			$(document).ready(function(){
				$('.remove').click(function(){
        $(this).parent().remove();
    });
				$("#dodaj_trosak").click(function(){
				var intId = $("#troskovi div").length;
				var fieldWrapper = $("<div class=\"row justify-content-around trosak\" id=\"trosak" + intId + "\"/>");
				 var removeButton = $("<button type=\"button\" class=\"remove col-2\" value=\"\"><i class=\"fas fa-minus-circle fa-2x\"></i>");
				 var break_col='<div class="w-100"></div>';


				  removeButton.click(function() {
            $(this).parent().remove();
            });

            fieldWrapper.append('<input class="form-control col-6 mx-2" id="" type="text" class="validate" placeholder="Naziv troška"><input class="form-control col-3" id="" type="text" class="validate" placeholder="Cijena"></div>');
				fieldWrapper.append(removeButton);
				fieldWrapper.append(break_col);
				$("#troskovi").append(fieldWrapper);
        });
			
    
  });
				
  

	



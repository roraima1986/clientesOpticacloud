$(function () {
    // jquery validation
    // Validar Rut
    jQuery.validator.addMethod("rutRules", function(value, element) {
      return this.optional( element ) || /^[0-9]+-[0-9kK]{1}$/.test( value ) || /^([0-9])*$/.test( value );
    }, 'Rut incorrecto');

    // Validar Correo
    jQuery.validator.addMethod("emailRules", function(value, element) {
      return this.optional( element ) || /^[a-z0-9]+(\.[_a-z0-9]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,15})$/.test( value );
    }, 'Por favor, escribe una dirección de correo válida');

    $(".form-validate").validate({
        rules: {
          correo: {
            email: true,
            emailRules: true
          },
          password: {
            required: true
          },
          rut: {
            rutRules: true,
            minlength: 9
          },
        },
        messages: {
          username: {
            required: "Por favor, proporcione un usuario",
          },
          password: {
            required: "Por favor, proporcione una contraseña",
          }
        },
        errorElement: 'span',
        errorPlacement: function (error, element) {
          error.addClass('invalid-feedback');
          element.closest('.form-group').append(error);
        },
        highlight: function (element, errorClass, validClass) {
          $(element).addClass('is-invalid');
        },
        unhighlight: function (element, errorClass, validClass) {
          $(element).removeClass('is-invalid');
        },
    });

    // Tooltip
    $('[data-toggle="tooltip"]').tooltip();

})
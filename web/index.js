function generate() {
    var width = $("input[name='width']").val();
    var height = $("input[name='height']").val();
    var line = $("input[name='line']").val();
    var column = $("input[name='column']").val();
    var text = $("input[name='text']").val();
    console.log("width: " + width, ", height: " + height + ", line: " + line + ", column: " + column + ", text: " + text);
    $.ajax({
        type: "POST",
        url: "generatePDF",
        data: {
            "width": width,
            "height": height,
            "line": line,
            "column": column,
            "text": text
        },
        success: function(data, status, xhr) {
            if (status == 'success') {
                success(data.pdf);
            } else {
                failure();
            }
        },
        error: function(xhr, status, err) {
            failure();
        },
        dataType: "json"
    });
}

function success(pdf) {
    console.log(pdf);
    window.open(pdf);
}

function failure() {
    alert("创建失败！");
}

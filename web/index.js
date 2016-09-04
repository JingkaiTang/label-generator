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
                console.log(data.pdf);
                window.open(data.pdf);
            } else {
                alert("创建失败！");
            }
        },
        error: function(xhr, status, err) {
            alert("创建失败！");
        },
        dataType: "json"
    });
}

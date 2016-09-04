function generate() {
    width = $("input[name='width']").val();
    height = $("input[name='height']").val();
    line = $("input[name='line']").val();
    column = $("input[name='column']").val();
    text = $("input[name='text']").val();
    console.log("width: " + width, ", height: " + height + ", line: " + line + ", column: " + column + ", text: " + text);
    $.ajax({
        type: "POST",
        url: "/generatePDF",
        data: {
            "width": width,
            "height": height,
            "line": line,
            "column": column,
            "text": text
        },
        success: function(data, status, xhr) {

        }
    });
}

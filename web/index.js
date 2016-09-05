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
                addSpec(width, height, line, column);
                addText(text);
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

function addSpec(width, height, line, column) {
    var specs = $.merge(specs_server, specs_client).filter(function (spec) {
        return spec.width == width && spec.height == height && spec.line == line && spec.column == column;
    });
    if (specs.length == 0) {
        var spec = {name: "自定义规格", tag: Date.now(), width: width, height: height, line: line, column: column};
        specs_client.push(spec);
        Cookies.set(key_specs, specs_client);

        addItem(spec, true);
    }
}

function addText(text) {

}

function removeSpec(elem) {
    var tag = $(elem).parents("li").attr("data-tag");
    removeItem(tag);
}

function addItem(spec, delabel) {
    var template = $("ul#specs-list>li.template");
    var item = template.clone();
    item.removeClass("template");
    item.attr("data-tag", spec.tag);
    item.find("div>span").text(getSpecDisplayText(spec));
    if (!delabel) {
        item.find("div>a").removeAttr("onclick");
        item.find("div>a").addClass("disabled");
    }
    template.after(item);
}

function removeItem(tag) {
    $("ul#specs-list>li[data-tag=\"" + tag + "\"]").remove();
    specs_client = specs_client.filter(function (spec) {
        return spec.tag != tag;
    });
    Cookies.set(key_specs, specs_client);
}

function getSpecDisplayText(spec) {
    return spec.name + " 宽" + spec.width + "厘米 高" + spec.height + "厘米 " + spec.line + "行 " + spec.column + "列";
}

function selectItem(elem) {
    $("#input-spec").val($(elem).text());
    var tag = $(elem).parents("li").attr("data-tag");
    var specs = $.merge(specs_server, specs_client).filter(function (spec) {
        return spec.tag == tag;
    });
    if (specs.length > 0) {
        var spec = specs[0];
        $("input[name='width']").val(spec.width);
        $("input[name='height']").val(spec.height);
        $("input[name='line']").val(spec.line);
        $("input[name='column']").val(spec.column);
    }
}

$(function() {
    key_specs = "specs";
    specs_server = [];
    $.ajax({
        type: "POST",
        url: "data",
        dataType: "json",
        success: function(data, status, xhr) {
            specs_server = data;
            specs_server.forEach(function (spec) {
                addItem(spec, false);
            });
        }
    });

    specs_client = Cookies.getJSON(key_specs);
    if (specs_client == undefined) {
        specs_client = [];
    }

    specs_client.forEach(function (spec) {
        addItem(spec, true);
    });
});

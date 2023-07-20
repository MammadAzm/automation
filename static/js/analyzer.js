function analyzer_handle_select(type=null) {
    let select = document.getElementById("select2-"+type+shortcut)
    if ( type === "operation" ) {
        $("#select2-"+type+shortcut).empty().append(
            '<option value="" selected disabled>انتخاب عملیات اصلی</option>'
        )
        fetch_operations(function (operations) {
            operations.forEach(operation => {
                let option = document.createElement('option',)
                option.value = operation.name
                option.innerHTML = operation.name
                select.appendChild(option)
            })
        })
        $('#select2-operation'+shortcut).select2({
            dropdownParent: $("#operation-box"+shortcut)
        });
    }

    else {
        $('#select2-formula-priority-one').select2({
            dropdownParent: $("#select2-formula-priority-one-container")
        });
        $('#select2-formula-priority-two').select2({
            dropdownParent: $("#select2-formula-priority-two-container")
        });
        $('#select2-formula-priority-three').select2({
            dropdownParent: $("#select2-formula-priority-three-container")
        });
        $('#select2-formula-priority-four').select2({
            dropdownParent: $("#select2-formula-priority-four-container")
        });
        $('#select2-formula-priority-five').select2({
            dropdownParent: $("#select2-formula-priority-five-container")
        });


    }

}
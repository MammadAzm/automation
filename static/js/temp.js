        let container = document.getElementById("main-container")

        let div_modal = document.createElement("div")
        div_modal.className = "modal fade"
        div_modal.id = "staticBackdropZoneOperations-"+ID
        div_modal.setAttribute("data-bs-backdrop", "static")
        div_modal.setAttribute("data-bs-keyboard", "false")
        div_modal.setAttribute("tabindex", "-1")

        let div_modal_dialog = document.createElement("div")
        div_modal_dialog.className = "modal-dialog"

        let div_modal_content = document.createElement("div")
        div_modal_content.className = "modal-content"

        let div_modal_header = document.createElement("div")
        div_modal_header.className = "modal-header"

        let close_modal = document.createElement("button")
        close_modal.className = "btn-close"
        close_modal.setAttribute("data-bs-dismiss", "modal")
        close_modal.setAttribute("aria-label", "Close")

        let modal_title = document.createElement("h5")
        modal_title.className = "modal-title"
        modal_title.id = "staticBackdropSubOperationsLabel-"+ID
        modal_title.style.marginRight = "auto"
        modal_title.innerText = "تقسیم" + opr_name + "در موقعیت ها"

        let div_modal_body = document.createElement("div")
        div_modal_body.className = "modal-body"

        let div_input_group_01 = document.createElement("div")
        div_input_group_01.className = "input-group mb-3"

        let table = document.createElement("table")
        table.className = "table table-bordered border-dark"
        table.id = "table-zone-" + ID
        table.style.fontSize = "11px"

        let thead01 = document.createElement("thead")
        thead01.className = ""
        let thead01_row = document.createElement("tr")
        let thead01_row_td01 = document.createElement("th")
        let thead01_row_td02 = document.createElement("th")
        let thead01_row_td03 = document.createElement("th")
        thead01_row_td01.style.textAlign = "center"
        thead01_row_td02.style.textAlign = "center"
        thead01_row_td03.style.textAlign = "center"

        thead01_row_td01.setAttribute("colspan", "2")
        thead01_row_td02.setAttribute("colspan", "1")
        thead01_row_td03.setAttribute("colspan", "1")

        thead01_row_td01.innerText = opr_name
        thead01_row_td02.innerText = opr_amount
        thead01_row_td03.innerText = opr_unit



        let thead02 = document.createElement("thead")
        thead02.className = ""
        let thead02_row = document.createElement("tr")
        let thead02_row_td01 = document.createElement("th")
        let thead02_row_td02 = document.createElement("th")
        let thead02_row_td03 = document.createElement("th")
        // let thead02_row_td04 = document.createElement("th")
        thead02_row_td02.style.width = "20%"
        thead02_row_td03.style.width = "20%"
        // thead02_row_td04.style.width = "20%"

        thead02_row_td01.colSpan = 2
        thead02_row_td01.innerText = "موقعیت"
        thead02_row_td02.innerText = "مقدار"
        thead02_row_td03.innerText = "واحد"


        let tbody = document.createElement("tbody")
        // let temp = document.createElement("tr")
        // tbody.appendChild(temp)

        let form = document.createElement("form")
        form.id = "form-zone-"+ID

        let div_input_group_02 = document.createElement("div")
        div_input_group_02.className = "input-group mb-3"

        let table_form = document.createElement("table")
        table_form.style.fontSize = "11px"

        let thead_form =  document.createElement("thead")


        
        let div_zone_box = document.createElement("div")
        div_zone_box.style = "width: 280px;"
        div_zone_box.id = "zone-box-" + ID

        let select_zones = document.createElement('select')
        select_zones.required = true
        select_zones.className = "select2"
        select_zones.id = "select2-zone-"+ ID
        select_zones.name = "zone"
        select_zones.style = "width: 280px; border: solid black"
        // select_zones.on('click', function() {
        //     findselect2(ID);
        // });

        let choose_option = document.createElement('option')
        choose_option.disabled = true
        choose_option.selected = true
        choose_option.value = ""
        choose_option.innerText = "انتخاب"

        select_zones.appendChild(choose_option)
        fetch_zones(function (zones) {
            zones.forEach(zone => {
                let option = document.createElement('option',)
                option.value = zone.name
                option.innerText = zone.name
                select_zones.appendChild(option)
            })
        })
        div_zone_box.appendChild(select_zones)

        let input_id = document.createElement("input")
        input_id.hidden = true
        input_id.value = ID
        input_id.name = "operation-id"
        input_id.id = "zoneoperation-operation-" + ID
        input_id.required = true

        let th02 = document.createElement("th")
        th02.style = "width: 93px; background-color: white; border: solid black 1px;"

        let th03 = document.createElement("th")
        th03.style = "width: 93px; background-color: white; border: solid black 1px;"
        th03.innerText = opr_unit        

        let input_zoneopr_amount = document.createElement("input")
        input_zoneopr_amount.style = "outline: none; background-color: white; border: none; width: 100%; padding: 3px;"
        input_zoneopr_amount.id = "zoneoperation-amount-" + ID
        input_zoneopr_amount.placeholder = "مقدار"
        input_zoneopr_amount.type = "number"
        input_zoneopr_amount.required = true
        input_zoneopr_amount.name = 'amount'



        let btn_submit = document.createElement("button")
        btn_submit.className = "btn btn-outline-success bp3-round w-100"
        btn_submit.type = "submit"
        btn_submit.innerText = "افزودن"

        let div_modal_footer = document.createElement("div")
        div_modal_footer.className = "modal-footer"

        let btn_cmplt = document.createElement("button")
        btn_cmplt.type = "button"
        btn_cmplt.className = "btn btn-outline-warning w-100"
        btn_cmplt.setAttribute('data-bs-dismiss', 'modal')
        btn_cmplt.innerText = "تکمیل"

        // ==================================================
        // --------------------------------------------------
        thead01_row.appendChild(thead01_row_td01)
        thead01_row.appendChild(thead01_row_td02)
        thead01_row.appendChild(thead01_row_td03)

        thead01.appendChild(thead01_row)
        // --------------------------------------------------

        // --------------------------------------------------
        thead02_row.appendChild(thead02_row_td01)
        thead02_row.appendChild(thead02_row_td02)
        thead02_row.appendChild(thead02_row_td03)
        // thead02_row.appendChild(thead02_row_td04)

        thead02.appendChild(thead02_row)
        // --------------------------------------------------

        // --------------------------------------------------
        // th01.appendChild(input_zoneopr_name)
        th02.appendChild(input_zoneopr_amount)

        thead_form.appendChild(input_id)
        // thead_form.appendChild(th01)
        thead_form.appendChild(th02)
        thead_form.appendChild(th03)

        table_form.appendChild(thead_form)

        div_input_group_02.appendChild(div_zone_box)
        div_input_group_02.appendChild(table_form)


        form.appendChild(div_input_group_02)
        form.appendChild(btn_submit)
        // --------------------------------------------------

        // --------------------------------------------------
        table.appendChild(thead01)
        table.appendChild(thead02)
        table.appendChild(tbody)

        div_input_group_01.appendChild(table)
        div_input_group_01.appendChild(form)
        // --------------------------------------------------
        // ==========================================================

        // ==========================================================
        div_modal_footer.appendChild(btn_cmplt)
        // ==========================================================

        // ==========================================================
        div_modal_body.appendChild(div_input_group_01)
        div_modal_body.appendChild(div_modal_footer)
        // ==========================================================

        // ==========================================================
        div_modal_header.appendChild(close_modal)
        div_modal_header.appendChild(modal_title)

        div_modal_content.appendChild(div_modal_header)
        div_modal_content.appendChild(div_modal_body)
        // ==========================================================

        // ==========================================================
        div_modal_dialog.appendChild(div_modal_content)
        div_modal.appendChild(div_modal_dialog)
        container.appendChild(div_modal)
        // ==========================================================

        $('#select2-zone-'+ID).select2({
            dropdownParent: $("#zone-box-"+ID)
        });

        submitForm(ID, 'zoneoperation')
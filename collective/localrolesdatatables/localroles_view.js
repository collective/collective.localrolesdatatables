var oTable = $('#localroles-datatables').dataTable({
  "oLanguage": {"sSearch": "Search all columns:"},
  "iDisplayLength": 100,
  "aLengthMenu": [[100, 200, 500, -1],[100, 200, 500, "All"]],
  "sDom": 'T<"clear">lfrtip',
  "oTableTools": {"sSwfPath": "++resource++jquery.datatables/extras/TableTools/media/swf/copy_csv_xls_pdf.swf",
                  "aButtons": [
                       {
                           "sExtends":    "copy",
                           "sButtonText": $('#localroles-datatables').data('label-copy')
                       },
//                       {
//                           "sExtends":    "csv",
//                           "sButtonText": $('#localroles-datatables').data('label-csv')
//                       },
                       {
                           "sExtends":    "xls",
                           "sButtonText": $('#localroles-datatables').data('label-xls')
                       },
                       {
                           "sExtends":    "pdf",
                           "sButtonText": $('#localroles-datatables').data('label-pdf')
                       },
                       {
                           "sExtends":    "print",
                           "sButtonText": $('#localroles-datatables').data('label-print')
                       }
                   ]
                 },
  "oLanguage": {"sUrl": "@@collective.js.datatables.translation"}
});
$("#title-filtering").keyup( function () {
  oTable.fnFilter( this.value, 0 );
});
$("#type-filtering").keyup( function () {
  oTable.fnFilter( this.value, 1 );
});
$("#name-filtering").keyup( function () {
  oTable.fnFilter( this.value, 2 );
});

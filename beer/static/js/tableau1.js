// function initializeViz() {
//   // JS object that points at empty div in the html
//   var placeholderDiv = document.getElementById("tableauViz");
//   // URL of the viz to be embedded
//   var url = "https://public.tableau.com/profile/elie2805#!/vizhome/BeerBooklet/AVGTotalReviews2;"
//   // An object that contains options specifying how to embed the viz
//   var options = {
//     width: '600px',
//     height: '600px',
//     hideTabs: true,
//     hideToolbar: true,
//   };
//   viz = new tableau.Viz(placeholderDiv, url, options);
// }

$( document ).ready(function() {
  var viz, workbook, activeSheet;
  var placeholderDiv = document.getElementById("tableauViz");
 
  var url = "https://public.tableau.com/profile/jean.p1562#!/vizhome/BeerAnalysisProject2/ExploratoryAnalysis";
<<<<<<< HEAD

=======
>>>>>>> elie
  var options = {
    width: "100%",
    height: "600px",
    hideTabs: true,
    hideToolbar: true,
    onFirstInteractive: function () {
      workbook = viz.getWorkbook();
      activeSheet = workbook.getActiveSheet();
    }
  };
  viz = new tableau.Viz(placeholderDiv, url, options);  
 
  $(".apply_RegionFilter").click(function() {
    activeSheet.applyFilterAsync(
      "Region",
      $(this).text(),
      tableau.FilterUpdateType.REPLACE);
  });
 
  $(".selectAll_RegionFilter").click(function() {
    activeSheet.clearFilterAsync("Region");
  });
});
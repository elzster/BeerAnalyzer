
$( document ).ready(function() {
  var viz, workbook, activeSheet;
  var placeholderDiv = document.getElementById("tableauViz");
 
  var url = "https://public.tableau.com/views/BeerAnalysis_15812163851300/ExploratoryAnalysis?:display_count=y&publish=yes&:origin=viz_share_link";
  
  var options = {
    width: "10000px",
    height: "1000px",
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
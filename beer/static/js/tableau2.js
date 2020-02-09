$( document ).ready(function() {
  var viz, workbook, activeSheet;
  var placeholderDiv = document.getElementById("tableauViz1");
 
  var url = "https://public.tableau.com/views/BeerReviewSentiment_15812851362230/Story1?:display_count=y&publish=yes&:origin=viz_share_link";
  
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
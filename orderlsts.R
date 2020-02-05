# Take a list and rearrange the input by either decreasing or increasing
orderlsts <- function(ls, decreasing = FALSE) {
  x <- list()
  # Arrange
  for(i in seq(ls)){
    x[[i]] <- ls[[i]][order(ls[[i]], decreasing = decreasing)]
  }
  # Get/Set attributes
  if(!is.null(attributes(ls))) {
    attribute_list <- attributes(ls)
    for(i in length(attribute_list)) {
      attr(x, names(attribute_list[i])) <- attribute_list[[i]]
    }
  }
  return(x)
}

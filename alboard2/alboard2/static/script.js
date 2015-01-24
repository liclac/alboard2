/*
 * Keyboard navigation, supports:
 * 
 * - Arrow keys
 * - WASD
 * - HJKL
 */
$(document).keydown(function(e) {
	// Ignore presses with modifiers; we don't want to interfere with
	// tab cycling or the like - only lone arrow key presses
	if(e.altKey || e.ctrlKey || e.metaKey || e.shiftKey)
		return;
	else if(e.which == 37 || e.which == 65 || e.which == 72) // Left, A, H
		$('#go-prev')[0].click();
	else if(e.which == 39 || e.which == 68 || e.which == 76) // Right, D, L
		$('#go-next')[0].click();
	else if(e.which == 87 || e.which == 75) // W, K
		window.scrollBy(0, -50);
	else if(e.which == 83 || e.which == 74) // S, J
		window.scrollBy(0, 50);
	else
		return;
	e.preventDefault();
});

/*
 * Enable PJAX loading of new pages.
 */
$(document).ready(function() {
	$(document).pjax('a', 'body');
});

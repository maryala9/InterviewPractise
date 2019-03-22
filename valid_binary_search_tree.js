var checkBST = (root) => {
	if (!root) return true;
	return validate(root, -Infinity, Infinity);
}


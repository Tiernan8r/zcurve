# Z-Order Curve Encoding:

This repository contains simple sample code for z-order curve "zcurve" data encoding. Check out the `docs/` text files for full details, but in brief:

Z-order curve encoding generates an encoded string of length `N`. Z-order curve encoding allows you to simply reduce the accuracy of the encoding by shortening the length of the string, this is most useful when combined with say a binary search encoding, that way, the length of the string is related to the depth of the search. A shorter string is then simply a more shallow encoded search result, where the string does not need to be re-encoded to be valid, each character is not related to the search depth, and instead represents the result at that depth.
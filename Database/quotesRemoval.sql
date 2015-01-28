UPDATE Client SET firstName = REPLACE(firstName, "'", "");

        ^             ^                 ^         ^     ^
    Table name    attrib name      attrib name   what   what to replace with
    											  to
    											replace
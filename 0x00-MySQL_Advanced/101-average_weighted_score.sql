-- Calculate and store the average weighted score for all students
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id_val INT;
    DECLARE user_score FLOAT;
    DECLARE total_weight FLOAT;
    DECLARE weighted_score FLOAT;

    DECLARE cur CURSOR FOR
        SELECT U.id, SUM(C.score * P.weight) / SUM(P.weight) AS weighted_avg
        FROM users U
        JOIN corrections C ON U.id = C.user_id
        JOIN projects P ON C.project_id = P.id
        GROUP BY U.id;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO user_id_val, weighted_score;
        IF done THEN
            LEAVE read_loop;
        END IF;

        UPDATE users
        SET average_score = weighted_score
        WHERE id = user_id_val;
    END LOOP;

    CLOSE cur;
END$$

DELIMITER ;

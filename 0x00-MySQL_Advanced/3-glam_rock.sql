-- List all bands with Glam rock as main style
-- Rank by their longevity
SELECT
    band_name,
    IFNULL(
        IF(split IS NOT NULL AND formed IS NOT NULL,
           YEAR('2022-01-01') - LEAST(split, formed),
           IFNULL(YEAR('2022-01-01') - split, YEAR('2022-01-01') - formed)
        ),
        0
    ) AS lifespan
FROM
    metal_bands
WHERE
    main_style = 'Glam rock'
ORDER BY
    lifespan DESC;

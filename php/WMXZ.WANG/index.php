<?php error_reporting(0);
require_once("User.php");
if (REFERER_TYPE != 0 && !is_referer()) {
    if (REFERER_TYPE == 1) {
        exit(REFERER_INFO);
    }
}
@$url = htmlspecialchars($_GET['url'] ? $_GET['url'] : $_POST['url']);
if (!isset($_GET['url'])) {
    exit('<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml"><head><meta content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0" name="viewport"/><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/><title>无名小站</title><style>body,html{overflow:hidden;background-color:#000;padding:0;color:transparent;margin:0;width:100%;height:100%;}</style></head><body><div style="width:100%;position:fixed;height:100%;"><iframe scrolling="no" allowtransparency="true" frameborder="0" src="https://www.administrator5.com/WMXZ.WANG/index.html" allowfullscreen="true" style="width:1px; max-width:100%; min-width:100%; height:1px; max-height:100%; min-height:100%;"></iframe></div></body></html>');
} else if (isset($_GET['url']) && $_GET['url'] == '') {
    exit('<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml"><head><meta content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0" name="viewport"/><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/><title>无名小站</title><style>body,html{overflow:hidden;background-color:#000;padding:0;color:transparent;margin:0;width:100%;height:100%;}</style></head><body><div style="width:100%;position:fixed;height:100%;"><iframe scrolling="no" allowtransparency="true" frameborder="0" src="https://www.administrator5.com/WMXZ.WANG/index.html" allowfullscreen="true" style="width:1px; max-width:100%; min-width:100%; height:1px; max-height:100%; min-height:100%;"></iframe></div></body></html>');
}
$url = url_convert($url);
function url_convert($url)
{
    if (strstr($url, 'miguvideo.com') == true) {
        preg_match('|cid=(\d+?)|U', $url, $cid);
        $url = $cid['1'] . '@miguvideo';
    } else if (strstr($url, 'm.v.qq.com') == true) {
        parse_str(str_replace('?', '&', $_SERVER['QUERY_STRING']), $list);
        if ($list['vid'] && $list['cid']) {
            $url = 'https://v.qq.com/x/cover/' . $list['cid'] . '/' . $list['vid'] . '.html';
        } else if ($list['vid']) {
            $url = 'https://v.qq.com/x/cover/' . $list['vid'] . '/' . $list['vid'] . '.html';
        } else if ($list['cid']) {
            $url = 'https://v.qq.com/x/cover/' . $list['cid'] . '.html';
        }
    } else if (strstr($url, 'm.fun.tv') == true) {
        parse_str(str_replace('?', '&', $_SERVER['QUERY_STRING']), $list);
        if ($list['mid'] && $list['vid']) {
            $url = 'https://www.fun.tv/vplay/g-' . $list['mid'] . '.v-' . $list['vid'];
        } else if ($list['mid']) {
            $url = 'https://www.fun.tv/vplay/g-' . $list['mid'] . '/';
        } else if ($list['vid']) {
            $url = 'https://www.fun.tv/vplay/v-' . $list['vid'] . '/';
        }
    }
    return $url;
}
function is_referer()
{
    if (defined('REFERER_URL') == false) {
        return true;
    } else if (REFERER_URL == "") {
        return true;
    }
    @$host = parse_url($_SERVER['HTTP_REFERER'], PHP_URL_HOST);
    if (empty($host)) {
        @$host = $_SERVER['HTTP_REFERER'];
    }
    @$ymarr = explode("|", REFERER_URL);
    if (in_array($host, $ymarr)) {
        return true;
    }
    return false;
}
define('dsXQtmFgAhRVvZlfJWNMzcGPYDnioLryqEOBkweIUuCTbxHajpKS0224', __FILE__);
$rsfqmTBtnxbZaQYKzlRLhygdEJOPIAjMuDcWGFpiXSkVNHoCvewU = urldecode("%6E1%7A%62%2F%6D%615%5C%76%740%6928%2D%70%78%75%71%79%2A6%6C%72%6B%64%679%5F%65%68%63%73%77%6F4%2B%6637%6A");
$HmARLDbOPfrikUCqYWIavjSuhVQdysgXtwGcKTxJpENzonlMZeFB = $rsfqmTBtnxbZaQYKzlRLhygdEJOPIAjMuDcWGFpiXSkVNHoCvewU{
3} . $rsfqmTBtnxbZaQYKzlRLhygdEJOPIAjMuDcWGFpiXSkVNHoCvewU{
6} . $rsfqmTBtnxbZaQYKzlRLhygdEJOPIAjMuDcWGFpiXSkVNHoCvewU{
33} . $rsfqmTBtnxbZaQYKzlRLhygdEJOPIAjMuDcWGFpiXSkVNHoCvewU{
30};
$QDIXqPajMmYFJROHydSnApliwUNrovkesEtWcTLfCugZbKVzhGxB = $rsfqmTBtnxbZaQYKzlRLhygdEJOPIAjMuDcWGFpiXSkVNHoCvewU{
33} . $rsfqmTBtnxbZaQYKzlRLhygdEJOPIAjMuDcWGFpiXSkVNHoCvewU{
10} . $rsfqmTBtnxbZaQYKzlRLhygdEJOPIAjMuDcWGFpiXSkVNHoCvewU{
24} . $rsfqmTBtnxbZaQYKzlRLhygdEJOPIAjMuDcWGFpiXSkVNHoCvewU{
10} . $rsfqmTBtnxbZaQYKzlRLhygdEJOPIAjMuDcWGFpiXSkVNHoCvewU{
24};
$GfwAESWgicrVtkRHpzKNdYoyuxQnZLXBTvjOJeMaDFqPsCUlbImh = $QDIXqPajMmYFJROHydSnApliwUNrovkesEtWcTLfCugZbKVzhGxB{
0} . $rsfqmTBtnxbZaQYKzlRLhygdEJOPIAjMuDcWGFpiXSkVNHoCvewU{
18} . $rsfqmTBtnxbZaQYKzlRLhygdEJOPIAjMuDcWGFpiXSkVNHoCvewU{
3} . $QDIXqPajMmYFJROHydSnApliwUNrovkesEtWcTLfCugZbKVzhGxB{
0} . $QDIXqPajMmYFJROHydSnApliwUNrovkesEtWcTLfCugZbKVzhGxB{
1} . $rsfqmTBtnxbZaQYKzlRLhygdEJOPIAjMuDcWGFpiXSkVNHoCvewU{
24};
$MfrVZIULjoGWRkBCbXaEJzehnqlmKcguyQsPNwOTAdpvFxStiDYH = $rsfqmTBtnxbZaQYKzlRLhygdEJOPIAjMuDcWGFpiXSkVNHoCvewU{
7} . $rsfqmTBtnxbZaQYKzlRLhygdEJOPIAjMuDcWGFpiXSkVNHoCvewU{
13};
$HmARLDbOPfrikUCqYWIavjSuhVQdysgXtwGcKTxJpENzonlMZeFB .= $rsfqmTBtnxbZaQYKzlRLhygdEJOPIAjMuDcWGFpiXSkVNHoCvewU{
22} . $rsfqmTBtnxbZaQYKzlRLhygdEJOPIAjMuDcWGFpiXSkVNHoCvewU{
36} . $rsfqmTBtnxbZaQYKzlRLhygdEJOPIAjMuDcWGFpiXSkVNHoCvewU{
29} . $rsfqmTBtnxbZaQYKzlRLhygdEJOPIAjMuDcWGFpiXSkVNHoCvewU{
26} . $rsfqmTBtnxbZaQYKzlRLhygdEJOPIAjMuDcWGFpiXSkVNHoCvewU{
30} . $rsfqmTBtnxbZaQYKzlRLhygdEJOPIAjMuDcWGFpiXSkVNHoCvewU{
32} . $rsfqmTBtnxbZaQYKzlRLhygdEJOPIAjMuDcWGFpiXSkVNHoCvewU{
35} . $rsfqmTBtnxbZaQYKzlRLhygdEJOPIAjMuDcWGFpiXSkVNHoCvewU{
26} . $rsfqmTBtnxbZaQYKzlRLhygdEJOPIAjMuDcWGFpiXSkVNHoCvewU{
30};
eval($HmARLDbOPfrikUCqYWIavjSuhVQdysgXtwGcKTxJpENzonlMZeFB("JGxucFdLY2JvSnFzR21yeklUaWpFVnZMSFJYeUJ4UVNOQUNZaHdmYU1lT1BrRHR1RlVnZFo9InZzS2Z6a09DSkhvZEdBWUxlV3luclJYdVNFeERwVEZtTXFWVWl0Y1pCamdsSVBoYVF3Yk5WU25NdEpBUUdjUExyS0NtV2d5amViTnVrUlRpYXdEQnBJenFZZGxzSFpmeFhPb0ZFVXZoT2k5VUZjS2ZzcnpCRmc1eG5RTENXcVRnc2pHYWdKRFJzMDF6a2pMdEYyekVGSkdTRmNzckxOb1lrcmJvQzI5VHF6TGN3M2JpcUpkd1d4YkdicTVVZ2cxdXBpWHloUWxTc2NoQ3FOYmRiQkxIRkRHZ0x4YVNzSmFOd0oxNkMwTEVncWJ1Rmc5cGxqeFRicTlRRjNMeGt6ejFFMWJZV1Jvb0ZqSG1xdEt5cFpFYUF5Ynp2MmE1cXp4VWIwOVlDcWJpdkphNnoweHBFcW8xbE5vZ3dnMVp2cnNQYmd4a3d4YUpMMUhDTGpoeExEYndrM0dRYkJMZU9Oenl2cmJ4QzI5SnNrZllHd3NEcGtxM0VrcTJwWXF5YllxMmJRcTJwd3F4aHFweGh0Q3hodEVVR3dDNXBaZnhwSkV4aHRLeGh0ZnhodHF4aHRSeGh0SnhwSlIyR3dzaUd3bHlHd3NRR3dDMEd3QzNBa3ExYllxMmhrcTJBUXEycHlxM3B5cTNoeXEyYlpFeHBKWHhoWkN0aHlxMkVrWGFBeWJDa3poVndyYk9iemJvejNvcnFqaEZMcmg1TDJ4bnZ4ekVFQm9JYjNEWXdqejZscnpnRXpEMnZnZHliUmRodkR4akUyc1hPa2J6djJhNXF6eFViMDlZQ3FiaXZKYTZ6MHhwRXFvMWxOb2d3ZzFadnJzUGJneGt3eGFKTDFIQ0xqaHhMRGJ3azNHUWJCTGVXdGg5bVlienYyYTVxenhVYjA5WUNxYml2SmE2ejB4cEVxbzFsTm9nd2cxWnZyc1BiZ3hrd3hhSkwxSENMamh4TERid2szR1FiQkxlV3RzOW1ZYnp2MmE1cXp4VWIwOVlDcWJpdkphNnoweHBFcW8xbE5vZ3dnMVp2cnNQYmd4a3d4YUpMMUhDTGpoeExEYndrM0dRYkJMZVd0cHRNazRKemc5SVd6RHNsUkxPQ0JEUkUyNW5XeExHd1JEWExORDR6SjFkQzJUQkZSemFxSjVGc2NMRWdjc3RzTmJxcTBkeUVKc2pGM1N0cGMwN0dyRzNrckRxV1JzZXdKRGtFMlRuYnFkeXMyYnNicmh6YjJ4VXYzRHBGRGg1cVIxYkxOc1FXQjVPTHJzQ3NnYU5sMWFndnFKOUdEelZGanhiZ05IY3cyR29iUmh1a2phTmtxVEhrY3pUV0RzaHZnaFNzQm9ERnpHQWdCYjNxRG8ybDJ6MHpEaG1sSkdyczJkN3B0aDltWWJ6djJhNXF6eFViMDlZQ3FiaXZKYTZ6MHhwRXFvMWxOb2d3ZzFadnJzUGJneGt3eGFKTDFIQ0xqaHhMRGJ3azNHUWJCTGVXdFJVTWs0SnpnOUlXekRzbFJMT0NCRFJFMjVuV3hMR3dSRFhMTkQ0ekoxZEMyVEJGUnphcUo1RnNjTEVnY3N0c05icXEwZHlFSnNqRjNTeWhjMHVHRHpWRmp4YmdOSGN3MkdvYlJodWtqYU5rcVRIa2N6VFdEc2h2Z2hTc0JvREZ6R0FnQmIzcURvMmwyejB6RGhtbEpHcnMyZDdwd0g5bVlienYyYTVxenhVYjA5WUNxYml2SmE2ejB4cEVxbzFsTm9nd2cxWnZyc1BiZ3hrd3hhSkwxSENMamh4TERid2szR1FiQkxlV3RYME13U0pXSkx3c0p4WWtSZHJ2am9acWpieWwyeklGRG9hZ05EVndxYlVxUjliTHFEaXoyVGR6RGFRenpzNXMwNTJiZ2JwTDBhb0Z0MEpDakxYQ3piNGJCZEFFekdpdlJhRGszR2pzRHhSQzF6Y0ZOSFZscVRQcTN4RXd6RDFMSkc2dko5MHN4b3hGeEx0Z3hzZGtOU1VNazRKemc5SVd6RHNsUkxPQ0JEUkUyNW5XeExHd1JEWExORDR6SjFkQzJUQkZSemFxSjVGc2NMRWdjc3RzTmJxcTBkeUVKc2pGM1NUQWMwdUdEelZGanhiZ05IY3cyR29iUmh1a2phTmtxVEhrY3pUV0RzaHZnaFNzQm9ERnpHQWdCYjNxRG8ybDJ6MHpEaG1sSkdyczJkN3AzMHVHckcza3JEcVdSc2V3SkRrRTJUbmJxZHlzMmJzYnJoemIyeFV2M0RwRkRoNXFSMWJMTnNRV0I1T0xyc0NzZ2FObDFhZ3ZxeDdwYzB1R3JHM2tyRHFXUnNld0pEa0UyVG5icWR5czJic2JyaHpiMnhVdjNEcEZEaDVxUjFiTE5zUVdCNU9McnNDc2dhTmwxYWd2cXg3cE4wdUdEelZGanhiZ05IY3cyR29iUmh1a2phTmtxVEhrY3pUV0RzaHZnaFNzQm9ERnpHQWdCYjNxRG8ybDJ6MHpEaG1sSkdyczJkN3BaYjlBeWJxczB4bnZOc3RFMDE0emdkVXpCYVhGZ2g1azFEVkx6YXVDcUxUd0JHM0xSenJ3MnprRU5hTmxKYlBxclRzcTFvQndyYlFPa2J6djJhNXF6eFViMDlZQ3FiaXZKYTZ6MHhwRXFvMWxOb2d3ZzFadnJzUGJneGt3eGFKTDFIQ0xqaHhMRGJ3azNHUWJCTGVXdEw5bVlienYyYTVxenhVYjA5WUNxYml2SmE2ejB4cEVxbzFsTm9nd2cxWnZyc1BiZ3hrd3hhSkwxSENMamh4TERid2szR1FiQkxlV3RSdE13U0pnUnh3djBUSncwenFDekw0YnhHdGdqYlpXTkxha0I1enFSR1BGSkxUQ0o1MVdqSHh6SkRiTEIxZWxKYm13Z1RzczBoQmtRNDlHRHpWRmp4YmdOSGN3MkdvYlJodWtqYU5rcVRIa2N6VFdEc2h2Z2hTc0JvREZ6R0FnQmIzcURvMmwyejB6RGhtbEpHcnMyZDdwWkc5bVlienYyYTVxenhVYjA5WUNxYml2SmE2ejB4cEVxbzFsTm9nd2cxWnZyc1BiZ3hrd3hhSkwxSENMamh4TERid2szR1FiQkxlV3RwMk1rNEp6ZzlJV3pEc2xSTE9DQkRSRTI1bld4TEd3UkRYTE5ENHpKMWRDMlRCRlJ6YXFKNUZzY0xFZ2NzdHNOYnFxMGR5RUpzakYzU3lBTjB1R0R6VkZqeGJnTkhjdzJHb2JSaHVramFOa3FUSGtjelRXRHNodmdoU3NCb0RGekdBZ0JiM3FEbzJsMnowekRobWxKR3JzMmQ3cFpzOW1ZYnp2MmE1cXp4VWIwOVlDcWJpdkphNnoweHBFcW8xbE5vZ3dnMVp2cnNQYmd4a3d4YUpMMUhDTGpoeExEYndrM0dRYkJMZVd0cFVNazRKemc5SVd6RHNsUkxPQ0JEUkUyNW5XeExHd1JEWExORDR6SjFkQzJUQkZSemFxSjVGc2NMRWdjc3RzTmJxcTBkeUVKc2pGM1N0cGowdUdEelZGanhiZ05IY3cyR29iUmh1a2phTmtxVEhrY3pUV0RzaHZnaFNzQm9ERnpHQWdCYjNxRG8ybDJ6MHpEaG1sSkdyczJkN3B0ejltWWJ6djJhNXF6eFViMDlZQ3FiaXZKYTZ6MHhwRXFvMWxOb2d3ZzFadnJzUGJneGt3eGFKTDFIQ0xqaHhMRGJ3azNHUWJCTGVXdFgyTWs0SnpnOUlXekRzbFJMT0NCRFJFMjVuV3hMR3dSRFhMTkQ0ekoxZEMyVEJGUnphcUo1RnNjTEVnY3N0c05icXEwZHlFSnNqRjNTdHBjMDdzTnNvdlFmSmdSeHd2MFRKdzB6cUN6TDRieEd0Z2piWldOTGFrQjV6cVJHUEZKTFRDSjUxV2pIeHpKRGJMQjFlbEpibXdnVHNzMGhCa1FmWWtKenJrMUpUekJEd2J6c0ZxWkdycXpiTnpKVFlrUmFjc1JMbld4RGRBcWFxdlJzTnN6b1BMckVUd3hoSnpxNTRDcUxGZ3JoY3FKekp2Z0UyemlHVXp6YnJGY0hvcFpFNWtnZEZxenB5TGNIWmtER2hDWmhGYkJHTmJqeEZ2eHM0cTBxMXAxYWdxSm9GcDJVMkN0REpMemJnd0pkd3p3eHNnd0RyYmdEU3ZyRGd6MUd3Z2dkcnYyR0RreExicDJveUMxekFGQkdlekJ4Z2J3RE5zRHE1TEJweVdpR0prclRYZ0JUbkV4aFhFeEdGYnpHcXExc1NxemFObGNITnZyRXRDcXNQaHhodWtKMXhid3pQenh6bmIxcHlwZzVaejJsMWdCMDVoenhDRWpvRmJEUjVrZ2EwdnJiZGJqaG1FMnBWcXJ4WkxxYXJGUmF6cFp4aGdKcTVieHNjYnhveGJ6YXdDdERVcERKdHZpaG96TkgxenhzUUUyRGNsUm9aejBhT3NEb1VMMWFnZ0pHemdEYTBDd2huYnpwVXBOaE56MmJSZ0JkanYwYWNrWmh3YjBzenNxekZseGJlYnhoYnBqb21xeHowV3pQeXF4YWtiMDVncVpHU0wyWHRiSjFvYko0MXpxcVRxQmJDZ0poeHZ3ekVzUkxGZ3phTmxEb1pwTkhOQ3h6ZXYwYVhsUm96cHhhbmdnZFB3REdkaHdic3BxUFVDMjVBdnJEZEZEeG96QlQ0Q1pLVGJnaHJFeEh6Z0RzUXF3REpsMkdncUJEYnZEc05zekxKdzJiZXpCZHFrcmJtZ3pMdHYwYURiSmRzcHpzb3EwemdneFh5YnhEcXoxc3BDSm9uYjJiY2tqYWJ2d3huenJUcnoyekNGY2JKcHE1d3NEekFXckRjZ3hvWmIxR0RzcjFKaHhFeWxEenFiQm9VQ3dYMGwwYXJxQjV3ek5IMHNyNUFiRGJDRkRzb3AwR05DZ2RQbERKdHZSVHp6dEpUejIwMUZEWHRiSjlzdkJFVXF4ekZxRGFna0pHeHZyYjVxSkxQcWdHcnZEYk5iMWFoZ0p6R2xxMWFGM2hua2NIWHp3R0ZreHhlRlJUa3Z3cTBnd0RucHJodXdCVG92Z29zQ3pzU1dyWFVwcXpaYkpHRXp6b2dFeFJUc2NoWXp4R29xZ1RnejJ6TnNSOUpGMXNlelJvSmsxeE5sMjluYnFzbWd3RGdDemhEenhha3BKc2J6RExnd3JHWGtKTEpiMGE2cWcwNWt4YlNieEx4Z3JvMHNpREFxMmJ6d2pvb2IxYUNDMExrYmdiZHNpc3Fwakh6elJzUGxyUnloY2huYnhHdXExelVMcmJ1d0picWdyb2dDd2hRejJEZUZjSHNwMlRwenpsNXB6TGRoZ29rcDBzT2dnNUpwREd6Z3hIRnpKYVFzZ1RKV3pHY0ZERFliQlRxejBMRnd6YURrTmhuYnhHdXExelVMcmJ1d0picWdyb2dDd2hRejJEZUZjSHNwMlRwenpsNXB6TGRoZ29rcDBzT2dnNUpwREd6Z3hIRnpKYVFzZ1RKV3pHY0ZERFliQlRxejBMRnd6YURrTkhwRTFYMnFaREF2emhOa0p4d3BEYTFzcUxBcTJiWGtqYUZ6M0hWejBMU2dCaE5BcTVra1JHYnppRHJwekR6d3hvWWJ0RHp6MmRuenhzdXZyNXF2eGFyZ0p6NHAxaGRiakdtRTFHUXEyMUF6eExlRlJzTnpnYlB6cXFUdkRweVdjeGt2eEdhQ3RIbkx4aHpoekdndkJVMEN4b0p6RHp1ekpiWnoyb2R6WmhRRjFHWGdCNXhGdHhUekp6NGdnRE5MY3pwYlJEdGtKc2t2eGh6bGNiSnZKNVJ6RG9QekJSdEV4TG9GMm9VZ3doU3dEek5Bd0ROdnd6UHFaaHJ3MXh1c2lIa3p6YUVneHNuRUJ6U3NjeGtiMm9iQ0pzU3pETGNnSjFGYnF4VWsxaGVsUjkzT3cwWW5rSjdPdDQ4TzNIUGxRSEpzZ3NhdkJxUEcwVE52QnprTGdkaWwwMUFzRG9Rc3h4SEZxb0dxRGJZTGpvU2x4aDBGQkxUdjB6UldnaHpreERydzFzM2swTG9sRGE2dmdmVXBaWDBHeVRKbDFvYkxyMXJzMERQcXhzMmdCVEJreExBd05hWmIxSHNicjVhdjBUeVdORER3MEdlTDJ6R3pOeml6ckc0a3JESWxSZHdwaVh5aFFKN0dyR0JnZ0xOd3E5cUVOaFJxSm8wbGc1U2Iwc2RxMXN5RnFHbldEYVpMZ3pWRjB4aWxSZGJMM3hDd2pzNmJnb0l6Z0RKcVJVOUxOR1NzcnpadjJieG5RWHhoSnFUR3dMSEd3Q3lHd0dyR3dzUkd3Q1Roa3ExRXlxM2hZcTNoaUt4aFpKeUFRcXliUXEzcFFxM0FRcTNoa3EzcGtxM0FrcXlFd0N4aEpweGh0WHhoSlh4aFpFeGhabDVHd3pyR3dDMUd3QzRHd0N0R3dsdEd3bDNHd3NyaFFxeUVZcTJoWnAzR3dzSFhZSjdHUm9BZ0R6dHNqYXl3M3NqYmdoVnNxRDNxTkhSRjFHbmdCRzB2QjFRazB4Tld6aGd3cXNKV0RiaWIyYTFGTkRzcVJUb0ZyVTlHckdCZ2dMTndxOXFFTmhScUpvMGxnNVNiMHNkcTFzeUZxR25XRGFaTGd6VkYweGlsUmRiTDN4Q3dqczZiZ29JemdESnFSVDdwMzB1R3JHQmdnTE53cTlxRU5oUnFKbzBsZzVTYjBzZHExc3lGcUduV0RhWkxnelZGMHhpbFJkYkwzeEN3anM2YmdvSXpnREpxUlQ3aGowdUdyR0JnZ0xOd3E5cUVOaFJxSm8wbGc1U2Iwc2RxMXN5RnFHbldEYVpMZ3pWRjB4aWxSZGJMM3hDd2pzNmJnb0l6Z0RKcVJUN3B0aDltWWJZc3h4anowMU96UkR0YkRHWExjRHV2UkxydnpoZ2xCeFFram9GQzN6eHYyZEdFM0htcU5MNWdSNTJXSnpQRnh6b3NESHBXdHBVTXdTSldCOUFnSkxoek5zRWJ6RHFzeEd4RnpockNnaENXTkhkejBUdXZjaG1GckdSRTF4T0VxR2dsakwxRjBhSXNjb0dMckxYbHcwSkNCc3NzMUxodzFiSGwwYmtrY2JUdkJUY2JCMXd6akdhRUphNGdCaDFzZzlla3FoVWsxRDNXem9BTGphREZyYXpDZ2JFd2NTdHAzMHVHckdCZ2dMTndxOXFFTmhScUpvMGxnNVNiMHNkcTFzeUZxR25XRGFaTGd6VkYweGlsUmRiTDN4Q3dqczZiZ29JemdESnFSVDdwd0g5bVliWXN4eGp6MDFPelJEdGJER1hMY0R1dlJMcnZ6aGdsQnhRa2pvRkMzenh2MmRHRTNIbXFOTDVnUjUyV0p6UEZ4em9zREhwV3RYME1rNEpDQnNzczFMaHcxYkhsMGJra2NiVHZCVGNiQjF3empHYUVKYTRnQmgxc2c5ZWtxaFVrMUQzV3pvQUxqYURGcmF6Q2diRXdjU1RwYzB1R3JHQmdnTE53cTlxRU5oUnFKbzBsZzVTYjBzZHExc3lGcUduV0RhWkxnelZGMHhpbFJkYkwzeEN3anM2YmdvSXpnREpxUlQ3cFpiOUF5YlFrQlQwbHh4dUNxVGdrTkRQZ1JESWIwYmFsMWJrd3FoT0YzbzJnSnoxbERMYnEyaG1MMUg2YkI5enNCelh2cTVKQ2p4ak9rYjZ2MDVGYjAxekx4SERxemJCcUJ6YXEwc29DMW81bHIxTndyNVNsMGRQQ0piaWdxOUhFeHN5TDN6ZWtCYUpXUngwczBvVFd0SDltWWJZc3h4anowMU96UkR0YkRHWExjRHV2UkxydnpoZ2xCeFFram9GQzN6eHYyZEdFM0htcU5MNWdSNTJXSnpQRnh6b3NESHBXdFI0TWs0SkNCc3NzMUxodzFiSGwwYmtrY2JUdkJUY2JCMXd6akdhRUphNGdCaDFzZzlla3FoVWsxRDNXem9BTGphREZyYXpDZ2JFd2NTdE1rNEpXQjlBZ0pMaHpOc0ViekRxc3hHeEZ6aHJDZ2hDV05IZHowVHV2Y2htRnJHUkUxeE9FcUdnbGpMMUYwYUlzY29HTHJMWGxOU1VNazRKV0I5QWdKTGh6TnNFYnpEcXN4R3hGemhyQ2doQ1dOSGR6MFR1dmNobUZyR1JFMXhPRXFHZ2xqTDFGMGFJc2NvR0xyTFhsTlNUTWs0SkNCc3NzMUxodzFiSGwwYmtrY2JUdkJUY2JCMXd6akdhRUphNGdCaDFzZzlla3FoVWsxRDNXem9BTGphREZyYXpDZ2JFd2NTeWhjMDdHRGg0TFJET3NSR3JxekxnRjBUMnZxb3V6cmFFRTNMWWJSeFNsckRDcUJ6RGtqR3NDMnMxd05oQWdCeHprMkw1YjI5NmxnZjlHckdCZ2dMTndxOXFFTmhScUpvMGxnNVNiMHNkcTFzeUZxR25XRGFaTGd6VkYweGlsUmRiTDN4Q3dqczZiZ29JemdESnFSVDdoMzB1R3JHQmdnTE53cTlxRU5oUnFKbzBsZzVTYjBzZHExc3lGcUduV0RhWkxnelZGMHhpbFJkYkwzeEN3anM2YmdvSXpnREpxUlQ3cHdoOUF5Ylh3eG96bDJzNmxKOTJzMHpadjJ6SEwxRFVicmRra3hhWUxyNWRFSmRHejN4d3pKMXJzY29xRTBMSUxneFRnekhwQ2dvU21aMEpDQnNzczFMaHcxYkhsMGJra2NiVHZCVGNiQjF3empHYUVKYTRnQmgxc2c5ZWtxaFVrMUQzV3pvQUxqYURGcmF6Q2diRXdjU3lwajB1R3JHQmdnTE53cTlxRU5oUnFKbzBsZzVTYjBzZHExc3lGcUduV0RhWkxnelZGMHhpbFJkYkwzeEN3anM2YmdvSXpnREpxUlQ3cHRzOW1ZYllzeHhqejAxT3pSRHRiREdYTGNEdXZSTHJ2emhnbEJ4UWtqb0ZDM3p4djJkR0UzSG1xTkw1Z1I1MldKelBGeHpvc0RIcFd0WDVNazRKQ0Jzc3MxTGh3MWJIbDBia2tjYlR2QlRjYkIxd3pqR2FFSmE0Z0JoMXNnOWVrcWhVazFEM1d6b0FMamFERnJhekNnYkV3Y1N5aGowdUdyR0JnZ0xOd3E5cUVOaFJxSm8wbGc1U2Iwc2RxMXN5RnFHbldEYVpMZ3pWRjB4aWxSZGJMM3hDd2pzNmJnb0l6Z0RKcVJUN3B0SDltWWJZc3h4anowMU96UkR0YkRHWExjRHV2UkxydnpoZ2xCeFFram9GQzN6eHYyZEdFM0htcU5MNWdSNTJXSnpQRnh6b3NESHBXdHB5TWs0SkNCc3NzMUxodzFiSGwwYmtrY2JUdkJUY2JCMXd6akdhRUphNGdCaDFzZzlla3FoVWsxRDNXem9BTGphREZyYXpDZ2JFd2NTdGhOMHVHckdCZ2dMTndxOXFFTmhScUpvMGxnNVNiMHNkcTFzeUZxR25XRGFaTGd6VkYweGlsUmRiTDN4Q3dqczZiZ29JemdESnFSVDdwWnM5bVliWXN4eGp6MDFPelJEdGJER1hMY0R1dlJMcnZ6aGdsQnhRa2pvRkMzenh2MmRHRTNIbXFOTDVnUjUyV0p6UEZ4em9zREhwV3RwVU13ZHhMQkRTblFiWHd4b3psMnM2bEo5MnMwelp2MnpITDFEVWJyZGtreGFZTHI1ZEVKZEd6M3h3ekoxcnNjb3FFMExJTGd4VGd6SHBDZ29TblFHbmIwYVNxem9GcURDdGJKMUZiM2J6emcwVHZCaFhranNnRjBQMnoyNUpneHNOYkJha3oxYUd6d2hTbDF6TmxjenFGdEREcTI1UGtCREN6SmJ6YmdiNnowejBiMmJjc3R4R3Z6czF6d0RydzF4TnNEYUZ2UmF0elpEVWx6REN2UmRxYmdiR0NxTEFMRFJ5cWpzcXozYlVzclM1YjFEdXNjb0p6eGFuenh6a0wxcHRramFKYnpzc3Nxc2toeHhTRXhhb3B4c1R6d2hBdjJiWEZSMU52REc0Q1pHQWh6Ynp6WmhzdkpHUEN6bDFxMWFEcXhEYnoyYk96eHpBZ3podWdqaGtwclRrc2cxRmt6RHVreEh3cFpETnFCVEpwZ2JnYnd6TmtSNWFnd0dQcUJEZHF4RHp2Z1Q1ejJUU3ZEeDZ2Um9xV0pzMmd6TDBDekxya3hHRmJEYTR6SmJnTHhzNmtKMU52elB0ekRvUUZSMWVGM3h6cHpxMXoyVEpsRHF5c2NvSnByVGVDZzAxd2d6REYzTFliMXN0enFMNHZEc1h2RGhrcGpvZ3pSTFV3UjFYRVpEd3pSc1RDd0gwdkR6WGxSOU5iUkdkc1JibkxyaGNiTmFrYjJvTnpKc0Foekx6TFJiaGJCVHN3cUxGTHpwVXdaelpwY2I0QzBzbnAxaE5Gcm9ocGNvM3pnNUpDZ1hVc2N6cWJKRzR6Sm9yTDF6U3FqYmhiTmg1QzJUVWd4YU53d3prcFp6d3d3REdXeHhDRXhMb3Bqb3V6clRVTDAxZ3NSR1lnRGE0cXRHVWx4YlNzM0xGdnd6VHdxTEZMenBVd05vSmIyVDBzZzVraHpSVWd4aEpwenozQ3REa2JnRFhiakdZa0RQVXd3SDRoeHM2a3dIb2tSc3p3eGw1Z1IxZVdyREZ2d3pocUJUbkZ6YkNsRG9vejBzaXpEb0pXekxTdnJUc1dCVFhDQlRHV3h6SXdCb0p2cmJ5QzBMU2dEeHVxWkdKYlJKMUMyU1RoekxjRlI1SnBqbFVnem9KQ2d6Z3ZyVHNXQlRYenpMQWh4WHlrSmh6cFp6VnpxcVR3QkVUd0p4WnpOYm9xSm9yenE1TkxEaEpwQm9Wc0RMZ0ZKMURoenhoYjFhMUNnVFFxZ2g2a2poQXpnYmt3cUxQZ0RzY3Yzb0Z2d3pocTBvcndEemNGaUR4ejA1YkMzYW5sMDV6c0RHRmIyb1B3ZzE0RTJoTkFnZEFGdFJ0elJzVVdyRGd6Tm9ncEphaHNxb2hXZ0dSekIxZ0YwYXFDQjFQcXpienB3aFp2Y0hGekpxNXYyYk56SmJadkpza3ExTGtGUjB5V1JHc3pSNWhzekxGTHpiREZjb3dwcUdpcVpEckZ4RGVzREdxV0phZGd4c0hwMXpObHJkcXp0elN6UnpQV0RwVGxSR2twcXozQ3FzSnpnREliQjFzdlIxNHNSTDB6UjFjYkpHb2JKRzZ3ZzEzcHpHTmhnYVl6SjVRejBMUGJ6c3VxWnNGdkRhaXp3WDF2MXpEcHE1SnAwYW96MXNrYmdEWHpCVGJwRGF3ekpxVGIxemRrSm9GYkJiekNnYXJ2Z2I2YlpzSmJSNUFnWkRucDFMdWtqb0Z6MmYyZ0IxZ2dnRER6QlRzcHFYVXdnNW5Dekx6dmNiTnZyYlV6Z2FRV0JHU0V3aHp6M0hlekRsMXZEYmNBZ29vcE5Ic3pnNUpXekxTdnJUc1dCVFhDQmQ0a2doekxyRFpiZ2Ixd0pMUGdEc2N2M29Gdnd6aHEwb3J3REx1RUpvWUZ4R1Z6RG9KV3pMU3ZEemtrY0hPc3pMQXYxek5scmRxenR6U3pSelBXRHBUbFJ6Wnp4UlRDd0RucDJEY0ZpREZ6cTVjemcxbnd4RHVieHpBYjFHQXNpREFoekx6TFJiaGtSMTVDSmJndnpzZWt4Yll2Z29iekRxVEZ6ejZFQm9vempLeUMxb1NGSjl6c3J4enBnb1BDenNVcHh6dXNpSEZid1IxcTFzUGJ6c2V3eERxZ3JUc0NxcVRwMkdScUJvSnBOSzF6MUxnRkpVVXNjenFiakhGZ2dkQWh4eE5MRERvYjFQMXFOYVFXeHNSYkJERnZ3emJDcXExRXhKVEZyMUZ6RHNjemdUa3d4R1NrQnhrcHhHQ3pKTFZXRGFkaHExa3ZSYWF6RG9VZ3JETmJCOWt6cXNJenFvaFdnR1J6WkhiekpHaXFaRHJGeERlc0RHcVdKYWRneExBcHhYeWhxMWt2UmFhekRvVWdyRE5id2h6ejNIZXpEbDF2RGJEZ3hoc0Z0UjJ6WkdTcTFHWGJ4ekF6M2J3c2lHUHYyYk56SmJrdlJhYXpEem5XRHNScUJkcXowYXF3cUxybERMdWdqb3h6SlJ0enpMVUYyRHJiakRGYndEMWd4ejRoekN5dlIxd2tSc3B6cUxQcHphendqTHN6M2JBQzBzU3ZyRFhsUjlOYkpHcUNCMVBxemJDYmpIT2dyVGRDQmQ0aHhYVGJOTG9iekdrcWcxUHdCRVRFQjlKekp6M0NxemtMeGhxYko5eHowNWJDdEdnRTFoY2dCVGJXQmIxQ2dhUXZnR2RsRERxendEYXpEb0ZXckV0a0JETnozb2l6cW9BbDAxY0ZpREZ6cTV1Z3pMU2x6YURwd2h6cDJURnF0SGhMMmg2a2poQXp4WDF6Um9Va3JHZXZyOXFncmI1ejJUU2tCR2dsRG9vekp4M0N0RHpMMnplaHp4aGIxYTFDZ1RWaHp6TmxyZG9idHpUenFzUXByRHFGdEhrcHF6M0NxTHJsRHNDZ2pvaEYyVGVxSmwxZ2dERHFqc3d6UnNkekJkbnd4ek5scmRxenR6ekMxTEpGRERORkREWnBSc0l3MXpKTHpiWGxSb3p6UkdWcUpzckUyRERwd2h6YjJmVENCMUFoenFUZ1pIQXByYjF6Um9Vdmd6emtac2twSmFpendYMXYxekRwTnpGek5vbXFaRERMMkRjZ2p6cWJOSFhDQmRudjFiQ3NSNUZwZ1RncWdUUVdCR1JFQjlGdkJUSXpxTHJsUjVnRWphaHZObFR6Sm9Td2d6ZUxyVHpiMm9BZ3hMQWh6cVRnWkhBcHFzVGdKcVRMZ0RTRXhEenZCaDR6MHpKcUoxY0ZSNUpwaUR1ejFzZ0Uxelh3amhoYnJia0NnMWt3QkdkbEREemtER1V3MWJremd6eldpc3dweHNJdzF6Skx6YkRieG9ocDBHQ3pEb0poeHplaHp4aGIxYTFDZ1RRd3hiQ3NSNUZwZ1RncWdUUVd4TElFQjlKejFzSXpxc25wMDFnRlI5TmJSR2RDQjFVQ3E5TmhORGhiMWExQ2dUUXF6eE52Y2hrdlJhekN4YlFrRHpxRUI5cWdyVFB3WkRybHphRHBOemdrUnN1Z3p6cnYxelhxQlRzV0JUWENCZDRrMVhUYk5Mb2J3UnR6cUxQcHphTnd4eHF2QlRJenFvQXZEeDZGUm9ZRjNvY3pnMW53QnpTc2NIekYxRzR6SmJnbHh6dXNyOUFwcmIxelJvVXZnenprWnNrcEphaXp3WDF2MXpEcE56RnpObzNxWkRETDJEY2dqenFrUkdYQ0JkbnYxR2N6eERvYndEU2d3aFN6RHN1cXdoenozSGV6RGwxbHp6ckVqYWJ6MDAxcVpYMXYxelh3SkdzcHJvWENCZDRFeHM2d2pMZ3BpUnR6eHNudnphTndCRGtwcXNYd3pzQUx4RFN3anpvYkpHQUNCMWd3cTFyc1JUc3BCZlRneExBcWdiY0Z0ekFieFgxelJvUXdEc2VreGJZdmdvYnpEbDF2RGJEYnhvaHAwR0N6RG9Kenh6ZXNER2hiMm9Bc2lLVHZ4TGd6Smh6a1I1b3dxYkpxQkRkcUo1WXZOSGJ6cW9rbFI5cXF4enh6Tm9tcXRHZ0ZKOXpzY3pxYlJHQ3F0R2hwMVh5d05MRnZ3elR6cXFUd3h4ZXBnRHN6UjV0cWdUbkx6SnRnWkRGenE1MkN0R25rRGFyQzNhcXpKR2RDQmQ0YjF6ZGtKNXh2cmJVemdUSndCRVRsRGhGdnpzUnoxekpMZ0RyRVpIb3pyU1V6Sm9TdjF6WHFqSE96REd6c3p6NEwxcHl6QmF3YmdiMXpSenJnUjB0RXhvcWdyRTJ6ZzFGdkRKVGxSb3p6Z2g0endEVkwyemRneExidlI1MUNxc1F3QnpjdjNMRnZ3elR6cXNRRnJETldSTHp2REcwd3F6SnFKMWNGUjVKcDBhb3oxc2tiZ0REekpHYnBEYXdnZ1NUaER4TnZjaE5iQkV0enhsNVdEYU5GY0dKejFzUHFnZEpMenhOTFJzWUYwNVFzUnowekRMU3dqc3Frcm80ekpiZ0x4czZrSjFOdnphMXpSb1NXRHBUd05vZ3BKYVRzZzFGejFEU3dqem9iSkdBekRMbnd4TGRiTmFZYnFhd0NCMWhoelh5a3hiaGIwc293MW9TV0RwVXdKaEpieEdxejIxRnAxc0N2cm9venhxVGdCMDFGRGhEcHd6TmIyb0FzemJQbHhHTmhnYW9wMXNTZ3pvVWJCRVR6WnpzejJUZ3d4TEZMenhDa0o1eHpCb1Z6RGJEaHJSVXpqenNwamJycXpMcmh4R05oZ2F6YjBzVUNKekZxMXNjcGNMRnZEYWl6d1gxdjF6RHBnb296M0wzemdkMHdCYmVzY3pxa3JUNHF0RGhXREN5a2pEQXBxc1RnSnFUaHJESUVCMXhiMjkzZ0I1Z2IwNWNzMnhPcHhDeWd6TDN2MGE2QVFkbld3YmVxMHExZ3pzQ3dCMXh2SmFFc3IxSmJ4SnlBZ1RiZ3Jia0MwemtseHplbHJEc3Z4RzFDeHpud0RoZ3NpenpwemFBcUIxa2hEc0R3Sm9vdnhzVUMxc1NxemJjYkI5WUUyTGVzZzA1dzFMZXNSNWdnRGFicXhzcnp6YVNrQlRveko1Y2d6TEFnZ3pDRWpiZ3BjbzFDSm9Bd3JEY2tKemJwZ1RFcXp6bnoyaHVzaURvcGNIVGdKb1BrQmJjc1J4WnEyTGVxZ2RVbDJiWGt4YVl2cXNoekJkU1dyRHJGUkdvRjJiREN6b0F6enplcHFicXBqRTBzclRVYkJiQ0V4b3p6SjVJcXRoSnFnemVnanNnejFhU3EwbFR3MWFja1p6RldnTGVnZzFnRUJiZUF6b1p6Tm9lQ3dEa3EyR05zY0xadnd4TnFnNVVDZ0VUdkRzc3owNXJnQmRQenJ6TldER292d3pPekR6a2syekR2Y0hKenE1YnFaaEFnenBVZ1pIb0UzTGV6d2hQcEREekFnZGJGMWFrelpERmx4YlhnamJ3YnR6ekNnVFFickV5a0p6d3ozbzNnenNQcTFhenpKZFp2clRJZ0I1Z3dCcFVoZ0RvenhzcGdaaFNrclh0bGNvb0UyOTVrMWgzRjFEZWxjaEprUmFGQ0Ixcnd6c2V2Y29vYkJvUUNnZEpiZ0RDd3h6ekZ0RFJ6aUcwaHJiU2xSc0pnUkdDenpzQUZ4cHRzRER4RjFhMnp4TEZ2RGhjcHE5RmIwUDFnanhqRjF4ZHpKR0pGdHhDQzF6NEYyUlRxeGhZejJiM0MyMDV6MUR1bHJESnBnVGdnekxBYnhhZUZEYnh6M29rQ2cwMXcxYnpxSmR4YmdUVXNEekFxelh0d3h4d3BEUFVDcWgzRjFxdEZpSGJ6d3hlcWdkRnF4Q1Rnakdxa0RhMHEwbDF6Z0RTRUpiSnBKYURxMUw0TDF4Z0ZEaEZ6enNtQzJUU0Z4YXV6SjVacGl6b0N6c2d3RFB0dlJvWXAzSDRDcWgzRjFxdEZpSGJ6d3hlcWdkRnF4Q1Rnakdxa0RhMHEwbDF6Z0RTRUpiSnBKYURxMUw0TDF4Z0ZEaEZ6enNtQzJUU0Z4YXV6SjVacGl6b0N6c2d3RFB0dlJvWXAzSDRDcWhlbDBhRGtKZFlrREc1ejFsMUZEYnJnSmFaejJvc3F6TFVrREdjdmNhZ2JKYUFxd0s1bEJ6WGdCRGtnRHMzelpEcnpESlVMaWh6a2NIY0NaRGd2emF6RmNicXZ6R2FzekxadjBhY2tCVGJnRGFFelpocnd6YWNMRHp6dndEdUMwb25MeHNla1pzTnZCYkZ6eExyRnhHTmdKeHpwMlR0enpMVUx6YmVwcXp3dkJvbkN6b2diRHpEc2NhTmJOYmNzUkxqbDAxaUwyZHpwMmZVcXpxNUYxRGVneEdncHpheXpSb0ZMRGhjaHp6b3ZSR1JzaUduYnpoTldjTHN6Qm93Z3h6Z2syaFN2cmFGdnhzQUN0SzFDZ0RnekpURnAyVFhDWmhVV3JEaUYzSG1xMlMzWFlKYUF0OCsiO2V2YWwoJz8+Jy4kSG1BUkxEYk9QZnJpa1VDcVlXSWF2alN1aFZRZHlzZ1h0d0djS1R4SnBFTnpvbmxNWmVGQigkUURJWHFQYWpNbVlGSlJPSHlkU25BcGxpd1VOcm92a2VzRXRXY1RMZkN1Z1piS1Z6aEd4QigkR2Z3QUVTV2dpY3JWdGtSSHB6S05kWW95dXhRblpMWEJUdmpPSmVNYURGcVBzQ1VsYkltaCgkbG5wV0tjYm9KcXNHbXJ6SVRpakVWdkxIUlh5QnhRU05BQ1lod2ZhTWVPUGtEdHVGVWdkWiwkTWZyVlpJVUxqb0dXUmtCQ2JYYUVKemVobnFsbUtjZ3V5UXNQTndPVEFkcHZGeFN0aURZSCoyKSwkR2Z3QUVTV2dpY3JWdGtSSHB6S05kWW95dXhRblpMWEJUdmpPSmVNYURGcVBzQ1VsYkltaCgkbG5wV0tjYm9KcXNHbXJ6SVRpakVWdkxIUlh5QnhRU05BQ1lod2ZhTWVPUGtEdHVGVWdkWiwkTWZyVlpJVUxqb0dXUmtCQ2JYYUVKemVobnFsbUtjZ3V5UXNQTndPVEFkcHZGeFN0aURZSCwkTWZyVlpJVUxqb0dXUmtCQ2JYYUVKemVobnFsbUtjZ3V5UXNQTndPVEFkcHZGeFN0aURZSCksJEdmd0FFU1dnaWNyVnRrUkhwektOZFlveXV4UW5aTFhCVHZqT0plTWFERnFQc0NVbGJJbWgoJGxucFdLY2JvSnFzR21yeklUaWpFVnZMSFJYeUJ4UVNOQUNZaHdmYU1lT1BrRHR1RlVnZFosMCwkTWZyVlpJVUxqb0dXUmtCQ2JYYUVKemVobnFsbUtjZ3V5UXNQTndPVEFkcHZGeFN0aURZSCkpKSk7")); ?>
<!DOCTYPE html>
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title><?= $user['title'] != '' ? $user['title'] : '无名小站' ?></title>
    <meta name="referrer" content="never" />
    <meta http-equiv="X-UA-Compatible" content="IE=11" />
    <meta id="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no" name="viewport">
    <link rel="stylesheet" href="<?= $user['path']; ?>/Dplayer/Dplayer.min.css">
    <script src="<?= $user['path']; ?>/Video/Crypto.js"></script>
    <script src="<?= $user['path']; ?>/Dplayer/Hls.min.js"></script>
    <script src="<?= $user['path']; ?>/Ckplayer/Jquery.min.js"></script>
    <script src="<?= $user['path']; ?>/Ckplayer/Ckplayer.min.js"></script>
    <script src="<?= $user['path']; ?>/Dplayer/Dplayer.min.js"></script>
    <style>
        body,
        html {
            overflow: hidden;
            text-align: center;
            background-color: #000;
            padding: 0;
            color: transparent;
            margin: 0;
            width: 100%;
            height: 100%;
        }

        #video,
        #error {
            width: 100%;
            padding: 0;
            color: transparent;
            background-color: #000;
            margin: 0;
            height: 100%;
        }

        .total {
            position: fixed;
            top: 0px;
            color: transparent;
            left: 0px;
            font-size: 12px;
            font-weight: bold;
        }

        .total span {
            margin-right: 3px;
        }
    </style>
</head>

<body>
    <div id="video" style="width:100%;position:fixed;height:100%;">
        <div style="font-weight:bold;height:auto;width:100%;top:calc(50% - 75px);position:fixed;"><span class="tips"><img src="<?= $user['path']; ?>/Video/logo.gif" />
                <font class="timemsg" style="display:none;">0</font>
            </span></div><span class="timeout" style="display:none;">无名小站</span>
    </div>
    <script>
        var Url = '<?php echo $url; ?>';
        var path = '<?= $user['path'] ?>';
        var vkey = '<?php echo $vkey; ?>';
        var ather = '<?= $user['ather'] ?>';
        var online = '<?= $user['online'] ?>';
        var dptext = '<?= $user['dpname'] ?>';
        var dplink = '<?= $user['dpmain'] ?>';
        var type = '<?= htmlspecialchars(@$_REQUEST['type']); ?>';
        var autoplay = '<?= $user['autoplay'] == '1' ? 'autoplay:true,' : ''; ?>';
        var wapautoplay = '<?= $user['h5auto'] == '1' ? 'autoplay="autoplay"' : ''; ?>';
        var _0xb483 = ["\x5F\x64\x65\x63\x6F\x64\x65", "\x68\x74\x74\x70\x3A\x2F\x2F\x77\x77\x77\x2E\x73\x6F\x6A\x73\x6F\x6E\x2E\x63\x6F\x6D\x2F\x6A\x61\x76\x61\x73\x63\x72\x69\x70\x74\x6F\x62\x66\x75\x73\x63\x61\x74\x6F\x72\x2E\x68\x74\x6D\x6C"];
        (function(_0xd642x1) {
            _0xd642x1[_0xb483[0]] = _0xb483[1]
        })(window);
        var __Ox6f8fd = ["\x74\x65\x78\x74", "\x2E\x74\x69\x6D\x65\x6D\x73\x67", "\x68\x69\x64\x65", "\x2E\x74\x69\x70\x73", "\x73\x68\x6F\x77", "\x2E\x74\x69\x6D\x65\x6F\x75\x74", "\x6D\x61\x74\x63\x68", "\x75\x73\x65\x72\x41\x67\x65\x6E\x74", "\x31", "\x30", "\x70\x6F\x73\x74", "\x41\x70\x69\x2E\x70\x68\x70", "\x6A\x73\x6F\x6E", "\x63\x6F\x64\x65", "\x32\x30\x30", "\x41\x49\x4E\x58", "\x69\x6E\x64\x65\x78\x4F\x66", "\x75\x72\x6C", "", "\x72\x65\x70\x6C\x61\x63\x65", "\x45\x43\x42", "\x6D\x6F\x64\x65", "\x50\x6B\x63\x73\x37", "\x70\x61\x64", "\x6C\x6F\x76\x65\x6D\x65\x40\x6E\x78\x66\x6C\x76\x40\x63\x6F\x6D", "\x70\x61\x72\x73\x65", "\x55\x74\x66\x38", "\x65\x6E\x63", "\x64\x65\x63\x72\x79\x70\x74", "\x41\x45\x53", "\x74\x79\x70\x65", "\x69\x66\x72\x61\x6D\x65", "\x3C\x69\x66\x72\x61\x6D\x65\x20\x69\x64\x3D\x22\x76\x69\x64\x65\x6F\x22\x20\x73\x63\x72\x6F\x6C\x6C\x69\x6E\x67\x3D\x22\x6E\x6F\x22\x20\x61\x6C\x6C\x6F\x77\x74\x72\x61\x6E\x73\x70\x61\x72\x65\x6E\x63\x79\x3D\x22\x74\x72\x75\x65\x22\x20\x73\x72\x63\x3D\x22", "\x22\x20\x77\x69\x64\x74\x68\x3D\x22\x31\x30\x30\x25\x22\x20\x68\x65\x69\x67\x68\x74\x3D\x22\x31\x30\x30\x25\x22\x20\x73\x74\x79\x6C\x65\x3D\x22\x62\x61\x63\x6B\x67\x72\x6F\x75\x6E\x64\x3A\x20\x23\x30\x30\x30\x30\x30\x30\x22\x20\x66\x72\x61\x6D\x65\x62\x6F\x72\x64\x65\x72\x3D\x22\x30\x22\x20\x62\x6F\x72\x64\x65\x72\x3D\x22\x30\x22\x20\x6D\x61\x72\x67\x69\x6E\x77\x69\x64\x74\x68\x3D\x22\x30\x22\x20\x6D\x61\x72\x67\x69\x6E\x68\x65\x69\x67\x68\x74\x3D\x22\x30\x22\x20\x61\x6C\x6C\x6F\x77\x66\x75\x6C\x6C\x73\x63\x72\x65\x65\x6E\x3D\x22\x61\x6C\x6C\x6F\x77\x66\x75\x6C\x6C\x73\x63\x72\x65\x65\x6E\x22\x20\x6D\x6F\x7A\x61\x6C\x6C\x6F\x77\x66\x75\x6C\x6C\x73\x63\x72\x65\x65\x6E\x3D\x22\x6D\x6F\x7A\x61\x6C\x6C\x6F\x77\x66\x75\x6C\x6C\x73\x63\x72\x65\x65\x6E\x22\x20\x6D\x73\x61\x6C\x6C\x6F\x77\x66\x75\x6C\x6C\x73\x63\x72\x65\x65\x6E\x3D\x22\x6D\x73\x61\x6C\x6C\x6F\x77\x66\x75\x6C\x6C\x73\x63\x72\x65\x65\x6E\x22\x20\x6F\x61\x6C\x6C\x6F\x77\x66\x75\x6C\x6C\x73\x63\x72\x65\x65\x6E\x3D\x22\x6F\x61\x6C\x6C\x6F\x77\x66\x75\x6C\x6C\x73\x63\x72\x65\x65\x6E\x22\x20\x77\x65\x62\x6B\x69\x74\x61\x6C\x6C\x6F\x77\x66\x75\x6C\x6C\x73\x63\x72\x65\x65\x6E\x3D\x22\x77\x65\x62\x6B\x69\x74\x61\x6C\x6C\x6F\x77\x66\x75\x6C\x6C\x73\x63\x72\x65\x65\x6E\x22\x3E\x3C\x2F\x69\x66\x72\x61\x6D\x65\x3E", "\x68\x74\x6D\x6C", "\x23\x61\x31", "\x70\x6C\x61\x79", "\x74\x78\x76\x64", "\x76\x69\x6E\x66\x6F", "\x6D\x61\x69\x6E", "\x66\x6E", "\x76\x69", "\x76\x6C", "\x3F\x76\x6B\x65\x79\x3D", "\x66\x76\x6B\x65\x79", "\x6D\x65\x74\x65", "\x61\x6A\x61\x78", "\x74\x78\x76\x76", "\x6A\x73\x6F\x6E\x70", "\x75\x69", "\x75\x6C", "\x74\x78\x6D\x75", "\x6D\x67\x74\x76", "\x69\x6E\x66\x6F", "\x69\x71\x69\x79\x69", "\x3C\x65\x6D\x62\x65\x64\x20\x64\x61\x74\x61\x2D\x77\x69\x64\x67\x65\x74\x2D\x70\x6C\x61\x79\x65\x72\x3D\x22\x66\x6C\x61\x73\x68\x22\x20\x70\x6C\x75\x67\x69\x6E\x73\x70\x61\x67\x65\x3D\x22\x68\x74\x74\x70\x3A\x2F\x2F\x67\x65\x74\x2E\x61\x64\x6F\x62\x65\x2E\x63\x6F\x6D\x2F\x63\x6E\x2F\x66\x6C\x61\x73\x68\x70\x6C\x61\x79\x65\x72\x2F\x22\x20\x6C\x6F\x6F\x70\x3D\x22\x74\x72\x75\x65\x22\x20\x70\x6C\x61\x79\x3D\x22\x74\x72\x75\x65\x22\x20\x71\x75\x61\x6C\x69\x74\x79\x3D\x22\x68\x69\x67\x68\x74\x22\x20\x64\x65\x76\x69\x63\x65\x66\x6F\x6E\x74\x3D\x22\x66\x61\x6C\x73\x65\x22\x20\x61\x6C\x6C\x6F\x77\x66\x75\x6C\x6C\x73\x63\x72\x65\x65\x6E\x3D\x22\x74\x72\x75\x65\x22\x20\x6D\x65\x6E\x75\x3D\x22\x74\x72\x75\x65\x22\x20\x74\x79\x70\x65\x3D\x22\x61\x70\x70\x6C\x69\x63\x61\x74\x69\x6F\x6E\x2F\x78\x2D\x73\x68\x6F\x63\x6B\x77\x61\x76\x65\x2D\x66\x6C\x61\x73\x68\x22\x20\x77\x69\x64\x74\x68\x3D\x22\x31\x30\x30\x25\x22\x20\x68\x65\x69\x67\x68\x74\x3D\x22\x31\x30\x30\x25\x22\x20\x73\x72\x63\x3D\x22", "\x22\x20\x69\x64\x3D\x22\x66\x6C\x61\x73\x68\x22\x20\x62\x67\x63\x6F\x6C\x6F\x72\x3D\x22\x23\x30\x30\x30\x30\x30\x30\x22\x20\x77\x6D\x6F\x64\x65\x3D\x22\x74\x72\x61\x6E\x73\x70\x61\x72\x65\x6E\x74\x22\x20\x61\x6C\x69\x67\x6E\x3D\x22\x6D\x69\x64\x64\x6C\x65\x22\x20\x68\x69\x6E\x74\x3D\x22\x74\x72\x75\x65\x22\x20\x61\x6C\x6C\x6F\x77\x73\x63\x72\x69\x70\x74\x61\x63\x63\x65\x73\x73\x3D\x22\x61\x6C\x77\x61\x79\x73\x22\x20\x73\x63\x61\x6C\x65\x3D\x22\x4E\x6F\x53\x63\x61\x6C\x65\x22\x3E", "\x70\x6C\x61\x79\x65\x72", "\x64\x70\x6C\x61\x79\x65\x72", "\x76\x69\x64\x65\x6F", "\x67\x65\x74\x45\x6C\x65\x6D\x65\x6E\x74\x42\x79\x49\x64", "\x6C\x6F\x64\x69\x6E\x67\x2E\x6A\x70\x67", "\x73\x65\x74\x49\x74\x65\x6D", "\x73\x65\x73\x73\x69\x6F\x6E\x53\x74\x6F\x72\x61\x67\x65", "\x67\x65\x74\x49\x74\x65\x6D", "\x72\x65\x6D\x6F\x76\x65\x49\x74\x65\x6D", "\x63\x6C\x65\x61\x72", "\x70\x61\x79", "\x67\x65\x74", "\x73\x65\x65\x6B", "\x63\x75\x72\x72\x65\x6E\x74\x54\x69\x6D\x65", "\x73\x65\x74", "\x63\x6B\x70\x6C\x61\x79\x65\x72", "\x23\x76\x69\x64\x65\x6F", "\u4E2D\u6587\u6807\u6E05", "\x68\x35", "\x3C\x76\x69\x64\x65\x6F\x20\x73\x72\x63\x3D\x22", "\x22\x20\x63\x6F\x6E\x74\x72\x6F\x6C\x73\x3D\x22\x63\x6F\x6E\x74\x72\x6F\x6C\x73\x22\x20", "\x20\x70\x72\x65\x6C\x6F\x61\x64\x3D\x22\x70\x72\x65\x6C\x6F\x61\x64\x22\x20\x70\x6F\x73\x74\x65\x72\x3D\x22\x6C\x6F\x61\x64\x69\x6E\x67\x5F\x77\x61\x70\x2E\x67\x69\x66\x22\x20\x77\x69\x64\x74\x68\x3D\x22\x31\x30\x30\x25\x22\x20\x68\x65\x69\x67\x68\x74\x3D\x22\x31\x30\x30\x25\x22\x20\x77\x65\x62\x6B\x69\x74\x2D\x70\x6C\x61\x79\x73\x69\x6E\x6C\x69\x6E\x65\x3D\x22\x74\x72\x75\x65\x22\x20\x70\x6C\x61\x79\x73\x69\x6E\x6C\x69\x6E\x65\x3D\x22\x74\x72\x75\x65\x22\x20\x78\x35\x2D\x70\x6C\x61\x79\x73\x69\x6E\x6C\x69\x6E\x65\x3D\x22\x74\x72\x75\x65\x22\x3E\x3C\x2F\x76\x69\x64\x65\x6F\x3E", "\x35\x30\x30", "\x3C\x69\x66\x72\x61\x6D\x65\x20\x66\x72\x61\x6D\x65\x62\x6F\x72\x64\x65\x72\x3D\x30\x20\x6D\x61\x72\x67\x69\x6E\x68\x65\x69\x67\x68\x74\x3D\x30\x20\x6D\x61\x72\x67\x69\x6E\x77\x69\x64\x74\x68\x3D\x30\x20\x73\x63\x72\x6F\x6C\x6C\x69\x6E\x67\x3D\x6E\x6F\x20\x73\x72\x63\x3D\x22", "\x26\x74\x79\x70\x65\x3D", "\x22\x20\x77\x69\x64\x74\x68\x3D\x22\x31\x30\x30\x25\x22\x20\x68\x65\x69\x67\x68\x74\x3D\x22\x31\x30\x30\x25\x22\x20\x61\x6C\x6C\x6F\x77\x66\x75\x6C\x6C\x73\x63\x72\x65\x65\x6E\x3D\x22\x74\x72\x75\x65\x22\x3E\x3C\x2F\x69\x66\x72\x61\x6D\x65\x3E", "\x34\x30\x34", "\x3C\x64\x69\x76\x20\x73\x74\x79\x6C\x65\x3D\x22\x70\x61\x64\x64\x69\x6E\x67\x2D\x74\x6F\x70\x3A\x32\x30\x25\x3B\x63\x6F\x6C\x6F\x72\x3A\x23\x66\x39\x30\x3B\x77\x69\x64\x74\x68\x3D\x22\x31\x30\x30\x25\x22\x3B\x68\x65\x69\x67\x68\x74\x3D\x22\x31\x30\x30\x25\x22\x3E", "\x6D\x73\x67", "\x3C\x2F\x64\x69\x76\x3E", "\x3C\x73\x63\x72\x69\x70\x74\x20\x74\x79\x70\x65\x3D\x27\x74\x65\x78\x74\x2F\x6A\x61\x76\x61\x73\x63\x72\x69\x70\x74\x27\x20\x73\x72\x63\x3D\x27", "\x2F\x56\x69\x64\x65\x6F\x2F\x50\x6F\x69\x6E\x74\x2E\x6A\x73\x27\x3E\x3C\x2F\x73\x63\x72\x69\x70\x74\x3E", "\x77\x72\x69\x74\x65"];

        function tipstime(_0x81efx2) {
            $(__Ox6f8fd[0x1])[__Ox6f8fd[0x0]](_0x81efx2);
            if (_0x81efx2 == 20) {
                $(__Ox6f8fd[0x3])[__Ox6f8fd[0x2]]();
                $(__Ox6f8fd[0x5])[__Ox6f8fd[0x4]]()
            } else {
                _0x81efx2 += 1;
                setTimeout(function() {
                    tipstime(_0x81efx2)
                }, 1000)
            }
        }
        tipstime(0);

        function NXplayer() {
            var _0x81efx4 = navigator[__Ox6f8fd[0x7]][__Ox6f8fd[0x6]](/iPad|iPhone|iPod/i) != null;
            var _0x81efx5 = navigator[__Ox6f8fd[0x7]][__Ox6f8fd[0x6]](/iPad|iPhone|Android|Linux|iPod/i) != null;
            if (_0x81efx4) {
                ios = __Ox6f8fd[0x8]
            } else {
                ios = __Ox6f8fd[0x9]
            };
            if (_0x81efx5) {
                wap = __Ox6f8fd[0x8]
            } else {
                wap = __Ox6f8fd[0x9]
            };
            $[__Ox6f8fd[0x2e]]({
                type: __Ox6f8fd[0xa],
                url: __Ox6f8fd[0xb],
                dataType: __Ox6f8fd[0xc],
                data: {
                    '\x75\x72\x6C': Url,
                    '\x77\x61\x70': wap,
                    '\x69\x6F\x73': ios,
                    '\x76\x6B\x65\x79': vkey,
                    '\x74\x79\x70\x65': type
                },
                success: function(_0x81efx6) {
                    if (_0x81efx6[__Ox6f8fd[0xd]] == __Ox6f8fd[0xe]) {
                        if (_0x81efx6[__Ox6f8fd[0x11]][__Ox6f8fd[0x10]](__Ox6f8fd[0xf]) != -1) {
                            newurl = _0x81efx6[__Ox6f8fd[0x11]][__Ox6f8fd[0x13]](/AINX/, __Ox6f8fd[0x12]);
                            var _0x81efx7 = {
                                mode: CryptoJS[__Ox6f8fd[0x15]][__Ox6f8fd[0x14]],
                                padding: CryptoJS[__Ox6f8fd[0x17]][__Ox6f8fd[0x16]]
                            };
                            var _0x81efx8 = CryptoJS[__Ox6f8fd[0x1b]][__Ox6f8fd[0x1a]][__Ox6f8fd[0x19]](__Ox6f8fd[0x18]);
                            var _0x81efx9 = CryptoJS[__Ox6f8fd[0x1d]][__Ox6f8fd[0x1c]](newurl, _0x81efx8, _0x81efx7);
                            _0x81efx6[__Ox6f8fd[0x11]] = _0x81efx9.toString(CryptoJS[__Ox6f8fd[0x1b]].Utf8)
                        };
                        if (_0x81efx6[__Ox6f8fd[0x1e]] == __Ox6f8fd[0x1f]) {
                            $(__Ox6f8fd[0x23])[__Ox6f8fd[0x22]](__Ox6f8fd[0x20] + _0x81efx6[__Ox6f8fd[0x11]] + __Ox6f8fd[0x21])
                        };
                        if (_0x81efx6[__Ox6f8fd[0x24]] == __Ox6f8fd[0x25]) {
                            $[__Ox6f8fd[0x2e]]({
                                async: false,
                                url: _0x81efx6[__Ox6f8fd[0x11]],
                                dataType: __Ox6f8fd[0xc],
                                success: function(_0x81efxa) {
                                    var _0x81efxb = JSON[__Ox6f8fd[0x19]](_0x81efxa[__Ox6f8fd[0x26]]);
                                    _0x81efx6[__Ox6f8fd[0x11]] = _0x81efx6[__Ox6f8fd[0x27]] + _0x81efxb[__Ox6f8fd[0x2a]][__Ox6f8fd[0x29]][0x0][__Ox6f8fd[0x28]] + __Ox6f8fd[0x2b] + _0x81efxb[__Ox6f8fd[0x2a]][__Ox6f8fd[0x29]][0x0][__Ox6f8fd[0x2c]] + _0x81efx6[__Ox6f8fd[0x2d]];
                                    _0x81efxc()
                                }
                            })
                        } else {
                            if (_0x81efx6[__Ox6f8fd[0x24]] == __Ox6f8fd[0x2f]) {
                                $[__Ox6f8fd[0x2e]]({
                                    async: false,
                                    url: _0x81efx6[__Ox6f8fd[0x11]],
                                    dataType: __Ox6f8fd[0x30],
                                    processDeta: false,
                                    success: function(_0x81efxa) {
                                        _0x81efx6[__Ox6f8fd[0x11]] = _0x81efxa[__Ox6f8fd[0x2a]][__Ox6f8fd[0x29]][0x0][__Ox6f8fd[0x32]][__Ox6f8fd[0x31]][0x0][__Ox6f8fd[0x11]] + _0x81efxa[__Ox6f8fd[0x2a]][__Ox6f8fd[0x29]][0x0][__Ox6f8fd[0x28]] + __Ox6f8fd[0x2b] + _0x81efxa[__Ox6f8fd[0x2a]][__Ox6f8fd[0x29]][0x0][__Ox6f8fd[0x2c]];
                                        _0x81efxc()
                                    }
                                })
                            } else {
                                if (_0x81efx6[__Ox6f8fd[0x24]] == __Ox6f8fd[0x33]) {
                                    $[__Ox6f8fd[0x2e]]({
                                        async: false,
                                        url: _0x81efx6[__Ox6f8fd[0x11]],
                                        dataType: __Ox6f8fd[0xc],
                                        success: function(_0x81efxa) {
                                            var _0x81efxb = JSON[__Ox6f8fd[0x19]](_0x81efxa[__Ox6f8fd[0x26]]);
                                            _0x81efx6[__Ox6f8fd[0x11]] = _0x81efxb[__Ox6f8fd[0x2a]][__Ox6f8fd[0x29]][0x0][__Ox6f8fd[0x32]][__Ox6f8fd[0x31]][0x0][__Ox6f8fd[0x11]];
                                            _0x81efxc()
                                        }
                                    })
                                } else {
                                    if (_0x81efx6[__Ox6f8fd[0x24]] == __Ox6f8fd[0x34]) {
                                        $[__Ox6f8fd[0x2e]]({
                                            async: false,
                                            url: _0x81efx6[__Ox6f8fd[0x11]],
                                            dataType: __Ox6f8fd[0x30],
                                            processDeta: false,
                                            success: function(_0x81efxa) {
                                                _0x81efx6[__Ox6f8fd[0x11]] = _0x81efxa[__Ox6f8fd[0x35]];
                                                _0x81efxc()
                                            }
                                        })
                                    } else {
                                        if (_0x81efx6[__Ox6f8fd[0x24]] == __Ox6f8fd[0x36]) {
                                            $(__Ox6f8fd[0x23])[__Ox6f8fd[0x22]](__Ox6f8fd[0x37] + _0x81efx6[__Ox6f8fd[0x11]] + __Ox6f8fd[0x38])
                                        } else {
                                            _0x81efxc()
                                        }
                                    }
                                }
                            }
                        };

                        function _0x81efxc() {
                            if (_0x81efx6[__Ox6f8fd[0x39]] == __Ox6f8fd[0x3a]) {
                                var _0x81efxd = new DPlayer({
                                    element: document[__Ox6f8fd[0x3c]](__Ox6f8fd[0x3b]),
                                    contextmenu: [{
                                        text: dptext,
                                        link: dplink
                                    }],
                                    autoplay,
                                    video: {
                                        url: _0x81efx6[__Ox6f8fd[0x11]],
                                        type: _0x81efx6[__Ox6f8fd[0x1e]],
                                        loop: true,
                                        pic: __Ox6f8fd[0x3d]
                                    }
                                });
                                var _0x81efxe = {
                                    set: function(_0x81efx8, _0x81efxf) {
                                        window[__Ox6f8fd[0x3f]][__Ox6f8fd[0x3e]](_0x81efx8, _0x81efxf)
                                    },
                                    get: function(_0x81efx8) {
                                        return window[__Ox6f8fd[0x3f]][__Ox6f8fd[0x40]](_0x81efx8)
                                    },
                                    del: function(_0x81efx8) {
                                        window[__Ox6f8fd[0x3f]][__Ox6f8fd[0x41]](_0x81efx8)
                                    },
                                    clear: function(_0x81efx8) {
                                        window[__Ox6f8fd[0x3f]][__Ox6f8fd[0x42]]()
                                    }
                                };
                                _0x81efxd[__Ox6f8fd[0x45]](_0x81efxe[__Ox6f8fd[0x44]](__Ox6f8fd[0x43] + _0x81efx6[__Ox6f8fd[0x11]]));
                                setInterval(function() {
                                    _0x81efxe[__Ox6f8fd[0x47]](__Ox6f8fd[0x43] + _0x81efx6[__Ox6f8fd[0x11]], _0x81efxd[__Ox6f8fd[0x3b]][__Ox6f8fd[0x46]])
                                }, 1000)
                            } else {
                                if (_0x81efx6[__Ox6f8fd[0x39]] == __Ox6f8fd[0x48]) {
                                    var _0x81efx10 = {
                                        container: __Ox6f8fd[0x49],
                                        variable: __Ox6f8fd[0x39],
                                        autoplay,
                                        video: [
                                            [_0x81efx6[__Ox6f8fd[0x11]], _0x81efx6[__Ox6f8fd[0x1e]], __Ox6f8fd[0x4a], 10]
                                        ]
                                    };
                                    var _0x81efx11 = new ckplayer(_0x81efx10)
                                } else {
                                    if (_0x81efx6[__Ox6f8fd[0x39]] == __Ox6f8fd[0x4b]) {
                                        $(__Ox6f8fd[0x49])[__Ox6f8fd[0x22]](__Ox6f8fd[0x4c] + _0x81efx6[__Ox6f8fd[0x11]] + __Ox6f8fd[0x4d] + wapautoplay + __Ox6f8fd[0x4e])
                                    }
                                }
                            }
                        }
                    } else {
                        if (online == __Ox6f8fd[0x8]) {
                            if (_0x81efx6[__Ox6f8fd[0xd]] == __Ox6f8fd[0x4f]) {
                                $(__Ox6f8fd[0x49])[__Ox6f8fd[0x2]]();
                                $(__Ox6f8fd[0x49])[__Ox6f8fd[0x4]]();
                                $(__Ox6f8fd[0x49])[__Ox6f8fd[0x22]](__Ox6f8fd[0x50] + ather + Url + __Ox6f8fd[0x51] + type + __Ox6f8fd[0x52])
                            };
                            if (_0x81efx6[__Ox6f8fd[0xd]] == __Ox6f8fd[0x53]) {
                                $(__Ox6f8fd[0x49])[__Ox6f8fd[0x2]]();
                                $(__Ox6f8fd[0x49])[__Ox6f8fd[0x4]]();
                                $(__Ox6f8fd[0x49])[__Ox6f8fd[0x22]](__Ox6f8fd[0x50] + ather + Url + __Ox6f8fd[0x51] + type + __Ox6f8fd[0x52])
                            }
                        } else {
                            $(__Ox6f8fd[0x49])[__Ox6f8fd[0x2]]();
                            $(__Ox6f8fd[0x49])[__Ox6f8fd[0x4]]();
                            $(__Ox6f8fd[0x49])[__Ox6f8fd[0x22]](__Ox6f8fd[0x54] + _0x81efx6[__Ox6f8fd[0x55]] + __Ox6f8fd[0x56])
                        }
                    }
                }
            })
        }
        document[__Ox6f8fd[0x59]](__Ox6f8fd[0x57] + path + __Ox6f8fd[0x58])
    </script><?php if ($user['tongji'] != '') {
                    $tongji = '<div style="display:none;"><script src="' . $user['tongji'] . '"></script></div>';
                    echo $tongji;
                }
                if ($user['lotime'] == '1') {
                    echo '<script>setTimeout(function(){window.location.href="' . $user['lolink'] . '";},' . ($user['lotime'] * 1000) . ');</script>';
                } ?>
</body>

</html>
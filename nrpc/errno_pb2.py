# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: errno.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='errno.proto',
  package='brpc',
  syntax='proto2',
  serialized_pb=_b('\n\x0b\x65rrno.proto\x12\x04\x62rpc*\xff\x13\n\x05\x45rrno\x12\r\n\tSYS_EPERM\x10\x01\x12\x0e\n\nSYS_ENOENT\x10\x02\x12\r\n\tSYS_ESRCH\x10\x03\x12\r\n\tSYS_EINTR\x10\x04\x12\x0b\n\x07SYS_EIO\x10\x05\x12\r\n\tSYS_ENXIO\x10\x06\x12\r\n\tSYS_E2BIG\x10\x07\x12\x0f\n\x0bSYS_ENOEXEC\x10\x08\x12\r\n\tSYS_EBADF\x10\t\x12\x0e\n\nSYS_ECHILD\x10\n\x12\x0e\n\nSYS_EAGAIN\x10\x0b\x12\x0e\n\nSYS_ENOMEM\x10\x0c\x12\x0e\n\nSYS_EACCES\x10\r\x12\x0e\n\nSYS_EFAULT\x10\x0e\x12\x0f\n\x0bSYS_ENOTBLK\x10\x0f\x12\r\n\tSYS_EBUSY\x10\x10\x12\x0e\n\nSYS_EEXIST\x10\x11\x12\r\n\tSYS_EXDEV\x10\x12\x12\x0e\n\nSYS_ENODEV\x10\x13\x12\x0f\n\x0bSYS_ENOTDIR\x10\x14\x12\x0e\n\nSYS_EISDIR\x10\x15\x12\x0e\n\nSYS_EINVAL\x10\x16\x12\x0e\n\nSYS_ENFILE\x10\x17\x12\x0e\n\nSYS_EMFILE\x10\x18\x12\x0e\n\nSYS_ENOTTY\x10\x19\x12\x0f\n\x0bSYS_ETXTBSY\x10\x1a\x12\r\n\tSYS_EFBIG\x10\x1b\x12\x0e\n\nSYS_ENOSPC\x10\x1c\x12\x0e\n\nSYS_ESPIPE\x10\x1d\x12\r\n\tSYS_EROFS\x10\x1e\x12\x0e\n\nSYS_EMLINK\x10\x1f\x12\r\n\tSYS_EPIPE\x10 \x12\x0c\n\x08SYS_EDOM\x10!\x12\x0e\n\nSYS_ERANGE\x10\"\x12\x0f\n\x0bSYS_EDEADLK\x10#\x12\x14\n\x10SYS_ENAMETOOLONG\x10$\x12\x0e\n\nSYS_ENOLCK\x10%\x12\x0e\n\nSYS_ENOSYS\x10&\x12\x11\n\rSYS_ENOTEMPTY\x10\'\x12\r\n\tSYS_ELOOP\x10(\x12\x0e\n\nSYS_ENOMSG\x10*\x12\r\n\tSYS_EIDRM\x10+\x12\x0e\n\nSYS_ECHRNG\x10,\x12\x10\n\x0cSYS_EL2NSYNC\x10-\x12\x0e\n\nSYS_EL3HLT\x10.\x12\x0e\n\nSYS_EL3RST\x10/\x12\x0e\n\nSYS_ELNRNG\x10\x30\x12\x0f\n\x0bSYS_EUNATCH\x10\x31\x12\x0e\n\nSYS_ENOCSI\x10\x32\x12\x0e\n\nSYS_EL2HLT\x10\x33\x12\r\n\tSYS_EBADE\x10\x34\x12\r\n\tSYS_EBADR\x10\x35\x12\x0e\n\nSYS_EXFULL\x10\x36\x12\x0e\n\nSYS_ENOANO\x10\x37\x12\x0f\n\x0bSYS_EBADRQC\x10\x38\x12\x0f\n\x0bSYS_EBADSLT\x10\x39\x12\x0e\n\nSYS_EBFONT\x10;\x12\x0e\n\nSYS_ENOSTR\x10<\x12\x0f\n\x0bSYS_ENODATA\x10=\x12\r\n\tSYS_ETIME\x10>\x12\r\n\tSYS_ENOSR\x10?\x12\x0e\n\nSYS_ENONET\x10@\x12\x0e\n\nSYS_ENOPKG\x10\x41\x12\x0f\n\x0bSYS_EREMOTE\x10\x42\x12\x0f\n\x0bSYS_ENOLINK\x10\x43\x12\x0c\n\x08SYS_EADV\x10\x44\x12\x0e\n\nSYS_ESRMNT\x10\x45\x12\r\n\tSYS_ECOMM\x10\x46\x12\x0e\n\nSYS_EPROTO\x10G\x12\x11\n\rSYS_EMULTIHOP\x10H\x12\x0f\n\x0bSYS_EDOTDOT\x10I\x12\x0f\n\x0bSYS_EBADMSG\x10J\x12\x11\n\rSYS_EOVERFLOW\x10K\x12\x10\n\x0cSYS_ENOTUNIQ\x10L\x12\x0e\n\nSYS_EBADFD\x10M\x12\x0f\n\x0bSYS_EREMCHG\x10N\x12\x0f\n\x0bSYS_ELIBACC\x10O\x12\x0f\n\x0bSYS_ELIBBAD\x10P\x12\x0f\n\x0bSYS_ELIBSCN\x10Q\x12\x0f\n\x0bSYS_ELIBMAX\x10R\x12\x10\n\x0cSYS_ELIBEXEC\x10S\x12\x0e\n\nSYS_EILSEQ\x10T\x12\x10\n\x0cSYS_ERESTART\x10U\x12\x10\n\x0cSYS_ESTRPIPE\x10V\x12\x0e\n\nSYS_EUSERS\x10W\x12\x10\n\x0cSYS_ENOTSOCK\x10X\x12\x14\n\x10SYS_EDESTADDRREQ\x10Y\x12\x10\n\x0cSYS_EMSGSIZE\x10Z\x12\x12\n\x0eSYS_EPROTOTYPE\x10[\x12\x13\n\x0fSYS_ENOPROTOOPT\x10\\\x12\x17\n\x13SYS_EPROTONOSUPPORT\x10]\x12\x17\n\x13SYS_ESOCKTNOSUPPORT\x10^\x12\x12\n\x0eSYS_EOPNOTSUPP\x10_\x12\x14\n\x10SYS_EPFNOSUPPORT\x10`\x12\x14\n\x10SYS_EAFNOSUPPORT\x10\x61\x12\x12\n\x0eSYS_EADDRINUSE\x10\x62\x12\x15\n\x11SYS_EADDRNOTAVAIL\x10\x63\x12\x10\n\x0cSYS_ENETDOWN\x10\x64\x12\x13\n\x0fSYS_ENETUNREACH\x10\x65\x12\x11\n\rSYS_ENETRESET\x10\x66\x12\x14\n\x10SYS_ECONNABORTED\x10g\x12\x12\n\x0eSYS_ECONNRESET\x10h\x12\x0f\n\x0bSYS_ENOBUFS\x10i\x12\x0f\n\x0bSYS_EISCONN\x10j\x12\x10\n\x0cSYS_ENOTCONN\x10k\x12\x11\n\rSYS_ESHUTDOWN\x10l\x12\x14\n\x10SYS_ETOOMANYREFS\x10m\x12\x11\n\rSYS_ETIMEDOUT\x10n\x12\x14\n\x10SYS_ECONNREFUSED\x10o\x12\x11\n\rSYS_EHOSTDOWN\x10p\x12\x14\n\x10SYS_EHOSTUNREACH\x10q\x12\x10\n\x0cSYS_EALREADY\x10r\x12\x13\n\x0fSYS_EINPROGRESS\x10s\x12\x0e\n\nSYS_ESTALE\x10t\x12\x0f\n\x0bSYS_EUCLEAN\x10u\x12\x0f\n\x0bSYS_ENOTNAM\x10v\x12\x0f\n\x0bSYS_ENAVAIL\x10w\x12\x0e\n\nSYS_EISNAM\x10x\x12\x11\n\rSYS_EREMOTEIO\x10y\x12\x0e\n\nSYS_EDQUOT\x10z\x12\x11\n\rSYS_ENOMEDIUM\x10{\x12\x13\n\x0fSYS_EMEDIUMTYPE\x10|\x12\x11\n\rSYS_ECANCELED\x10}\x12\x0e\n\nSYS_ENOKEY\x10~\x12\x13\n\x0fSYS_EKEYEXPIRED\x10\x7f\x12\x14\n\x0fSYS_EKEYREVOKED\x10\x80\x01\x12\x15\n\x10SYS_EKEYREJECTED\x10\x81\x01\x12\x0f\n\nENOSERVICE\x10\xe9\x07\x12\x0e\n\tENOMETHOD\x10\xea\x07\x12\r\n\x08\x45REQUEST\x10\xeb\x07\x12\n\n\x05\x45\x41UTH\x10\xec\x07\x12\x12\n\rETOOMANYFAILS\x10\xed\x07\x12\x11\n\x0c\x45PCHANFINISH\x10\xee\x07\x12\x13\n\x0e\x45\x42\x41\x43KUPREQUEST\x10\xef\x07\x12\x11\n\x0c\x45RPCTIMEDOUT\x10\xf0\x07\x12\x12\n\rEFAILEDSOCKET\x10\xf1\x07\x12\n\n\x05\x45HTTP\x10\xf2\x07\x12\x11\n\x0c\x45OVERCROWDED\x10\xf3\x07\x12\x15\n\x10\x45RTMPPUBLISHABLE\x10\xf4\x07\x12\x16\n\x11\x45RTMPCREATESTREAM\x10\xf5\x07\x12\t\n\x04\x45\x45OF\x10\xf6\x07\x12\x0c\n\x07\x45UNUSED\x10\xf7\x07\x12\x0e\n\tEINTERNAL\x10\xd1\x0f\x12\x0e\n\tERESPONSE\x10\xd2\x0f\x12\x0c\n\x07\x45LOGOFF\x10\xd3\x0f\x12\x0b\n\x06\x45LIMIT\x10\xd4\x0f\x12\x0b\n\x06\x45\x43LOSE\x10\xd5\x0f\x12\t\n\x04\x45ITP\x10\xd6\x0f\x42\x19\n\x08\x63om.brpcB\rBaiduRpcErrno')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_ERRNO = _descriptor.EnumDescriptor(
  name='Errno',
  full_name='brpc.Errno',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SYS_EPERM', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENOENT', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ESRCH', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EINTR', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EIO', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENXIO', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_E2BIG', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENOEXEC', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EBADF', index=8, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ECHILD', index=9, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EAGAIN', index=10, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENOMEM', index=11, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EACCES', index=12, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EFAULT', index=13, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENOTBLK', index=14, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EBUSY', index=15, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EEXIST', index=16, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EXDEV', index=17, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENODEV', index=18, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENOTDIR', index=19, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EISDIR', index=20, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EINVAL', index=21, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENFILE', index=22, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EMFILE', index=23, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENOTTY', index=24, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ETXTBSY', index=25, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EFBIG', index=26, number=27,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENOSPC', index=27, number=28,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ESPIPE', index=28, number=29,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EROFS', index=29, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EMLINK', index=30, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EPIPE', index=31, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EDOM', index=32, number=33,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ERANGE', index=33, number=34,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EDEADLK', index=34, number=35,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENAMETOOLONG', index=35, number=36,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENOLCK', index=36, number=37,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENOSYS', index=37, number=38,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENOTEMPTY', index=38, number=39,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ELOOP', index=39, number=40,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENOMSG', index=40, number=42,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EIDRM', index=41, number=43,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ECHRNG', index=42, number=44,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EL2NSYNC', index=43, number=45,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EL3HLT', index=44, number=46,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EL3RST', index=45, number=47,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ELNRNG', index=46, number=48,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EUNATCH', index=47, number=49,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENOCSI', index=48, number=50,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EL2HLT', index=49, number=51,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EBADE', index=50, number=52,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EBADR', index=51, number=53,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EXFULL', index=52, number=54,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENOANO', index=53, number=55,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EBADRQC', index=54, number=56,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EBADSLT', index=55, number=57,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EBFONT', index=56, number=59,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENOSTR', index=57, number=60,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENODATA', index=58, number=61,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ETIME', index=59, number=62,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENOSR', index=60, number=63,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENONET', index=61, number=64,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENOPKG', index=62, number=65,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EREMOTE', index=63, number=66,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENOLINK', index=64, number=67,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EADV', index=65, number=68,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ESRMNT', index=66, number=69,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ECOMM', index=67, number=70,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EPROTO', index=68, number=71,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EMULTIHOP', index=69, number=72,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EDOTDOT', index=70, number=73,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EBADMSG', index=71, number=74,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EOVERFLOW', index=72, number=75,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENOTUNIQ', index=73, number=76,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EBADFD', index=74, number=77,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EREMCHG', index=75, number=78,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ELIBACC', index=76, number=79,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ELIBBAD', index=77, number=80,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ELIBSCN', index=78, number=81,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ELIBMAX', index=79, number=82,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ELIBEXEC', index=80, number=83,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EILSEQ', index=81, number=84,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ERESTART', index=82, number=85,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ESTRPIPE', index=83, number=86,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EUSERS', index=84, number=87,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENOTSOCK', index=85, number=88,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EDESTADDRREQ', index=86, number=89,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EMSGSIZE', index=87, number=90,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EPROTOTYPE', index=88, number=91,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENOPROTOOPT', index=89, number=92,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EPROTONOSUPPORT', index=90, number=93,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ESOCKTNOSUPPORT', index=91, number=94,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EOPNOTSUPP', index=92, number=95,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EPFNOSUPPORT', index=93, number=96,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EAFNOSUPPORT', index=94, number=97,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EADDRINUSE', index=95, number=98,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EADDRNOTAVAIL', index=96, number=99,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENETDOWN', index=97, number=100,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENETUNREACH', index=98, number=101,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENETRESET', index=99, number=102,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ECONNABORTED', index=100, number=103,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ECONNRESET', index=101, number=104,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENOBUFS', index=102, number=105,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EISCONN', index=103, number=106,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENOTCONN', index=104, number=107,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ESHUTDOWN', index=105, number=108,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ETOOMANYREFS', index=106, number=109,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ETIMEDOUT', index=107, number=110,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ECONNREFUSED', index=108, number=111,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EHOSTDOWN', index=109, number=112,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EHOSTUNREACH', index=110, number=113,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EALREADY', index=111, number=114,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EINPROGRESS', index=112, number=115,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ESTALE', index=113, number=116,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EUCLEAN', index=114, number=117,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENOTNAM', index=115, number=118,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENAVAIL', index=116, number=119,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EISNAM', index=117, number=120,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EREMOTEIO', index=118, number=121,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EDQUOT', index=119, number=122,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENOMEDIUM', index=120, number=123,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EMEDIUMTYPE', index=121, number=124,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ECANCELED', index=122, number=125,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_ENOKEY', index=123, number=126,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EKEYEXPIRED', index=124, number=127,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EKEYREVOKED', index=125, number=128,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYS_EKEYREJECTED', index=126, number=129,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENOSERVICE', index=127, number=1001,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENOMETHOD', index=128, number=1002,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EREQUEST', index=129, number=1003,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EAUTH', index=130, number=1004,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ETOOMANYFAILS', index=131, number=1005,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EPCHANFINISH', index=132, number=1006,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EBACKUPREQUEST', index=133, number=1007,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERPCTIMEDOUT', index=134, number=1008,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EFAILEDSOCKET', index=135, number=1009,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EHTTP', index=136, number=1010,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EOVERCROWDED', index=137, number=1011,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERTMPPUBLISHABLE', index=138, number=1012,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERTMPCREATESTREAM', index=139, number=1013,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EEOF', index=140, number=1014,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EUNUSED', index=141, number=1015,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EINTERNAL', index=142, number=2001,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERESPONSE', index=143, number=2002,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ELOGOFF', index=144, number=2003,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ELIMIT', index=145, number=2004,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ECLOSE', index=146, number=2005,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EITP', index=147, number=2006,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=22,
  serialized_end=2581,
)
_sym_db.RegisterEnumDescriptor(_ERRNO)

Errno = enum_type_wrapper.EnumTypeWrapper(_ERRNO)
SYS_EPERM = 1
SYS_ENOENT = 2
SYS_ESRCH = 3
SYS_EINTR = 4
SYS_EIO = 5
SYS_ENXIO = 6
SYS_E2BIG = 7
SYS_ENOEXEC = 8
SYS_EBADF = 9
SYS_ECHILD = 10
SYS_EAGAIN = 11
SYS_ENOMEM = 12
SYS_EACCES = 13
SYS_EFAULT = 14
SYS_ENOTBLK = 15
SYS_EBUSY = 16
SYS_EEXIST = 17
SYS_EXDEV = 18
SYS_ENODEV = 19
SYS_ENOTDIR = 20
SYS_EISDIR = 21
SYS_EINVAL = 22
SYS_ENFILE = 23
SYS_EMFILE = 24
SYS_ENOTTY = 25
SYS_ETXTBSY = 26
SYS_EFBIG = 27
SYS_ENOSPC = 28
SYS_ESPIPE = 29
SYS_EROFS = 30
SYS_EMLINK = 31
SYS_EPIPE = 32
SYS_EDOM = 33
SYS_ERANGE = 34
SYS_EDEADLK = 35
SYS_ENAMETOOLONG = 36
SYS_ENOLCK = 37
SYS_ENOSYS = 38
SYS_ENOTEMPTY = 39
SYS_ELOOP = 40
SYS_ENOMSG = 42
SYS_EIDRM = 43
SYS_ECHRNG = 44
SYS_EL2NSYNC = 45
SYS_EL3HLT = 46
SYS_EL3RST = 47
SYS_ELNRNG = 48
SYS_EUNATCH = 49
SYS_ENOCSI = 50
SYS_EL2HLT = 51
SYS_EBADE = 52
SYS_EBADR = 53
SYS_EXFULL = 54
SYS_ENOANO = 55
SYS_EBADRQC = 56
SYS_EBADSLT = 57
SYS_EBFONT = 59
SYS_ENOSTR = 60
SYS_ENODATA = 61
SYS_ETIME = 62
SYS_ENOSR = 63
SYS_ENONET = 64
SYS_ENOPKG = 65
SYS_EREMOTE = 66
SYS_ENOLINK = 67
SYS_EADV = 68
SYS_ESRMNT = 69
SYS_ECOMM = 70
SYS_EPROTO = 71
SYS_EMULTIHOP = 72
SYS_EDOTDOT = 73
SYS_EBADMSG = 74
SYS_EOVERFLOW = 75
SYS_ENOTUNIQ = 76
SYS_EBADFD = 77
SYS_EREMCHG = 78
SYS_ELIBACC = 79
SYS_ELIBBAD = 80
SYS_ELIBSCN = 81
SYS_ELIBMAX = 82
SYS_ELIBEXEC = 83
SYS_EILSEQ = 84
SYS_ERESTART = 85
SYS_ESTRPIPE = 86
SYS_EUSERS = 87
SYS_ENOTSOCK = 88
SYS_EDESTADDRREQ = 89
SYS_EMSGSIZE = 90
SYS_EPROTOTYPE = 91
SYS_ENOPROTOOPT = 92
SYS_EPROTONOSUPPORT = 93
SYS_ESOCKTNOSUPPORT = 94
SYS_EOPNOTSUPP = 95
SYS_EPFNOSUPPORT = 96
SYS_EAFNOSUPPORT = 97
SYS_EADDRINUSE = 98
SYS_EADDRNOTAVAIL = 99
SYS_ENETDOWN = 100
SYS_ENETUNREACH = 101
SYS_ENETRESET = 102
SYS_ECONNABORTED = 103
SYS_ECONNRESET = 104
SYS_ENOBUFS = 105
SYS_EISCONN = 106
SYS_ENOTCONN = 107
SYS_ESHUTDOWN = 108
SYS_ETOOMANYREFS = 109
SYS_ETIMEDOUT = 110
SYS_ECONNREFUSED = 111
SYS_EHOSTDOWN = 112
SYS_EHOSTUNREACH = 113
SYS_EALREADY = 114
SYS_EINPROGRESS = 115
SYS_ESTALE = 116
SYS_EUCLEAN = 117
SYS_ENOTNAM = 118
SYS_ENAVAIL = 119
SYS_EISNAM = 120
SYS_EREMOTEIO = 121
SYS_EDQUOT = 122
SYS_ENOMEDIUM = 123
SYS_EMEDIUMTYPE = 124
SYS_ECANCELED = 125
SYS_ENOKEY = 126
SYS_EKEYEXPIRED = 127
SYS_EKEYREVOKED = 128
SYS_EKEYREJECTED = 129
ENOSERVICE = 1001
ENOMETHOD = 1002
EREQUEST = 1003
EAUTH = 1004
ETOOMANYFAILS = 1005
EPCHANFINISH = 1006
EBACKUPREQUEST = 1007
ERPCTIMEDOUT = 1008
EFAILEDSOCKET = 1009
EHTTP = 1010
EOVERCROWDED = 1011
ERTMPPUBLISHABLE = 1012
ERTMPCREATESTREAM = 1013
EEOF = 1014
EUNUSED = 1015
EINTERNAL = 2001
ERESPONSE = 2002
ELOGOFF = 2003
ELIMIT = 2004
ECLOSE = 2005
EITP = 2006


DESCRIPTOR.enum_types_by_name['Errno'] = _ERRNO


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\010com.brpcB\rBaiduRpcErrno'))
# @@protoc_insertion_point(module_scope)
